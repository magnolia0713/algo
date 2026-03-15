T = int(input())

for _ in range(T):
    n = int(input())

    if n <= 3:
        if n == 1:
            ans = 1

        elif n == 2:
            ans = 2

        elif n == 3:
            ans = 3

    else:
        p = n // 3
        ans = 0
        for i in range(p+1):
            temp = n - i * 3

            ans += temp // 2 + 1

    print(ans)