N = int(input())

if N == 1:
    print(input())

else:
    beverage = [0]

    for _ in range(N):
        i = int(input())
        beverage.append(i)


    memo = [[0,0] for _ in range(N+1)]
    memo[1][0] = beverage[1]
    memo[2][0] = beverage[2]
    memo[2][1] = beverage[1] + beverage[2]

    for i in range(3,N+1):
        memo[i][0] = max(memo[i-2][0], memo[i-2][1], memo[i-3][1]) + beverage[i]
        memo[i][1] = memo[i-1][0] + beverage[i]

    print(max(memo[N][0],memo[N][1], memo[N-1][0], memo[N-1][1]))
