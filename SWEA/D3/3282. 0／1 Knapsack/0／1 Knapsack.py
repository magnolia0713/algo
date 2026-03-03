

test_case = int(input())


for tc in range(1, test_case+1):
    n, k = map(int, input().split())
    item_box = []

    dp = [0] * (k+1)
    # k를 보고 물건의 최상 value를 갱신.
    for _ in range(n):
        v, c = map(int, input().split())
        a_max = 0
        for i in range(0,k+1):
            if i - v >= 0:
                dp[i-v] = max(dp[i-v], dp[i] + c)

    print(f"#{tc} {max(dp)}")