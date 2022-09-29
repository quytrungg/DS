#check if we can make the array become non-decreasing by changing only 1 element or not
def check(lst):
    flag = 0
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            flag += 1
    return True if flag == 1 else False
        
print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False