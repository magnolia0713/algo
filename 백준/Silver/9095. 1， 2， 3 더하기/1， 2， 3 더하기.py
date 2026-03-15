def calc(n):
    if n <= 3:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
    else:
        if memo[n] == 0:
            memo[n] = calc(n-1) + calc(n-2) + calc(n-3)
            return memo[n]
        else:
            return memo[n]

T = int(input())
for tc in range(1, T+1):
    memo = [0] * 11
    num = int(input())
    print(calc(num))