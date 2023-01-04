def hIndex(publications):
    h = 1
    while True:
        count = 0
        for i in publications:
            if i >= h:
                count += 1
        if count != h and h < len(publications):
            h += 1
        else:
            break
    return h

print(hIndex([5, 3, 3, 1, 0]))
# 3