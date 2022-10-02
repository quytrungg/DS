from tokenize import Octnumber


def coin_flip(n, H, T):
    if(n == 0):
        return 1
    if(H == 0 or T == 0):
        return 0
    return coin_flip(n - 1, H - 1, T) + coin_flip(n - 1, H, T - 1)


print(coin_flip(3, 2, 1))
