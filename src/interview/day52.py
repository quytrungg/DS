def getBonuses(performance):
    result = [1 for _ in range(len(performance))]
    for i in range(len(performance)):
        if i == 0:
            if performance[i] > performance[i+1]:
                result[i] += 1
            else:
                continue
        if i == len(performance)-1:
            if performance[i] > performance[i-1]:
                result[i] += 1
            else:
                break
        if performance[i] > performance[i-1]:
            result[i] += 1
        if performance[i] > performance[i+1]:
            result[i] += 1
    return result

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]