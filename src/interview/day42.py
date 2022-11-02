from numpy import sort

def running_median(stream):
    sum = 0
    for i in range(len(stream)):
        temp_arr = sort(stream[:i+1])
        if len(temp_arr) % 2 == 1:
            print(temp_arr[int(len(temp_arr)/2)])
        else:
            print((temp_arr[int(len(temp_arr)/2)]+temp_arr[int(len(temp_arr)/2 - 1)])/2)

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2