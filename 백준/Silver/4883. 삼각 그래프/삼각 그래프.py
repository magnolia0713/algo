from sys import setrecursionlimit

setrecursionlimit(100000)

def DP(r,c):
    if memo[r][c] != -1000000000:
        return memo[r][c]

    if c == 0:
        memo[r][c] = min(DP(r-1,0), DP(r-1,1)) + matrix[r][c]

    elif c == 1:
        memo[r][c] = min(DP(r-1,0), DP(r-1,1), DP(r-1,2), DP(r,0)) + matrix[r][c]

    elif c == 2:
        memo[r][c] = min(DP(r-1,1), DP(r-1,2), DP(r,1)) + matrix[r][c]

    return memo[r][c]

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1000000000]*3 for _ in range(N)]
    memo[0][0] = 10000
    memo[0][1] = matrix[0][1]
    memo[0][2] = matrix[0][1] + matrix[0][2]
    result = DP(N-1,1)
    print(f"{tc}. {result}")