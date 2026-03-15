n = int(input())
memo = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n+1)]
memo[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, n+1):

    memo[i][0] = memo[i-1][1]
    memo[i][1] = (memo[i - 1][0] + memo[i - 1][2]) % 1000000000
    memo[i][2] = (memo[i - 1][1] + memo[i - 1][3]) % 1000000000
    memo[i][3] = (memo[i - 1][2] + memo[i - 1][4]) % 1000000000
    memo[i][4] = (memo[i - 1][3] + memo[i - 1][5]) % 1000000000
    memo[i][5] = (memo[i - 1][4] + memo[i - 1][6]) % 1000000000
    memo[i][6] = (memo[i - 1][5] + memo[i - 1][7]) % 1000000000
    memo[i][7] = (memo[i - 1][6] + memo[i - 1][8]) % 1000000000
    memo[i][8] = (memo[i - 1][7] + memo[i - 1][9]) % 1000000000
    memo[i][9] = memo[i - 1][8]

print(sum(memo[n])%1000000000)
