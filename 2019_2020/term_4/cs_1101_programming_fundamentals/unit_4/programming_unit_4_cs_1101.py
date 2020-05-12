def is_divisible(a, b):
    return a % b == 0

def is_power(a, b):
    if a == b or b == 1:
        return True
    elif is_divisible(a, b) and is_power(b, a / b):
        return True
    else:
        return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))