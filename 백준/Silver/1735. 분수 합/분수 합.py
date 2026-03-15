def com_divisor(a, b):
    while b:
        a, b = b, a % b

    return a

up_a, down_a = map(int, input().split())
up_b, down_b = map(int, input().split())

com_ab = com_divisor(down_a, down_b)
down_ab = down_a * down_b // com_ab

up_ab = up_a * (down_b // com_ab) + up_b * (down_a // com_ab)
com_fraction = com_divisor(up_ab, down_ab)

print(up_ab//com_fraction, down_ab//com_fraction)