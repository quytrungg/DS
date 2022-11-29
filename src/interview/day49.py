def calcAngle(h, m):
    return int(abs(m/5 - h)*30 - (1/12 * m/60)*360)

assert calcAngle(3, 30) == 75
assert calcAngle(12, 30) == 165