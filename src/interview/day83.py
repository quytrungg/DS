def shortest_path(file_path):
    path = file_path.split('/')
    result = []
    for i in path:
        if i == '..':
            result = result[:-1]
        elif i == '.':
            continue
        else:
            result.append(i)
    return '/'.join(result)

print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/