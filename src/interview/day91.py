import math

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False