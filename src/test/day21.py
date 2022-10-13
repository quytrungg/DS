def merge(intervals):
    result = []
    for i in range(len(intervals)):
        temp = intervals[i]
        for j in range(len(intervals)):
            if intervals[j][0] < temp[0] and intervals[j][1] > temp[1]:
                temp = intervals[j]
        if temp not in result:
            result.append(temp)

    return result

def merge2(intervals):
    n = len(intervals)
    result = intervals.copy()
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            # i is subset of j
            if intervals[i][0] > intervals[j][0] and intervals[i][1] < intervals[j][1]:
                result[i] = None
                break
            # i is superset of j
            elif intervals[i][0] < intervals[j][0] and intervals[i][1] > intervals[j][1]:
                result[j] = None
            elif intervals[i][1] > intervals[j][0] and intervals[i][1] < intervals[j][1]:
                result[i] = None
                result[j] = (intervals[i][0], intervals[j][1])
            elif intervals[i][0] > intervals[j][0] and intervals[i][0] < intervals[j][1]:
                result[i] = None
                result[j] = (intervals[j][0], intervals[i][1])
            
    result.remove(None)
    return list(filter(lambda x: x != None, result))
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]