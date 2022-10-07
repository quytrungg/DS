def maximum_product_of_three(list):
    new = list.copy()
    new.sort()
    a = new[0] * new[1] * new[-1]
    b = new[-1] * new[-2] * new[-3]
    if a > b:
        return a
    else:
        return b