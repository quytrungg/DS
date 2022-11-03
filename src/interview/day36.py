def isSorted(words, order):
    for i in range(len(words)-1):
        idx = 0
        if len(words[i]) < len(words[i+1]):
            temp = len(words[i])
            if idx < temp:
                pass


    return 

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True