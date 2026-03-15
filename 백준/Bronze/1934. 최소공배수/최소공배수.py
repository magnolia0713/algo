def least_common(a, b):
    num = 45000

    while num >= 1:
        if a % num == 0 and b % num == 0:
            comm_divisor = num
            break
        num -= 1

    print(a * b // comm_divisor)





T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    least_common(a, b)