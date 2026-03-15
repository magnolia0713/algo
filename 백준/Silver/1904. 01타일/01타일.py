n = int(input())

if n == 1:
    print(1)

else:
    memo = [0] * (n+1)

    memo[1] = 1
    memo[2] = 2

    for i in range(3,n+1):
        memo[i] = memo[i-1]%15746 + memo[i-2]%15746

    print(memo[n]%15746)