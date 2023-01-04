BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]

def utf8_validator(bytes):
    return

print(utf8_validator([0b00000000]))
# True
print(utf8_validator([0b00000000, 10000000]))
# False
print(utf8_validator([0b11000000, 10000000]))
# True