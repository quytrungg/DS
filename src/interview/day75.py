def is_shifted(a, b):
    for _ in range(len(a)):
        a = a[1:] + a[0]
        if a == b:
            return True
    return False
  
print(is_shifted('abcde', 'cdeab'))
# True