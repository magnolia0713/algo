def com_divisor(a, b):
    while b:
        a, b = b, a % b

    return a

a, b = map(int, input().split())

print(a * b //com_divisor(a, b))