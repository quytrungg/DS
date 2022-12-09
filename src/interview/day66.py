def rearrangeString(s):
    result = [i for i in s]
    for i in range(len(result)-2):
        for j in range(i+1, len(result)-1):
            if result[j] == result[j+1]:
                result[i], result[j] = result[j], result[i]
                break
    return ''.join(result)

print(rearrangeString('abbccc'))
# cbcabc