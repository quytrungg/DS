# question: given a string of calculation, evaluate the result

def eval(expression):
    RPN = []
    S = []
    
    # Convert to RPN
    for i in expression.split(' '):
        if i.isnumeric():
            RPN.append(i)
        elif i == '+' or i == '-' or i == '*' or i == '/':
            if S:
                while S[-1] == '+' or S[-1] == '-' or S[-1] == '*' or S[-1] == '/':
                    if not((S[-1] == '+' or S[-1] == '-') and (i == '*' or i == '/')):
                        RPN.append(S.pop())
                    if not S:
                        break
            S.append(i)
        elif i == '(':
            S.append(i)
        elif i == ')':
            while S[-1] != '(':
                RPN.append(S.pop())
            S.pop()
            
    for i in reversed(S):
        RPN.append(S.pop())
    
    print(RPN)
    print(S)
    
    # Calculate
    for i in RPN:
        if i.isnumeric():
            S.append(i)
        else:
            b = int(S.pop())
            a = 0
            if S:
                a = int(S.pop())
            
            if i == '+':
                S.append(a + b)
            elif i == '-':
                S.append(a - b)
            elif i == '*':
                S.append(a * b)
            elif i == '/':
                S.append(a / b)
            
    return S[0]

print(eval('- (3 + ( 2 - 1 ) )'))
# -4