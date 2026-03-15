def DP(level, r, c):
    if r < 0 or c < 0:
        return 0

    if memo[level][r][c] != 0:
        return memo[level][r][c]

    if matrix[r][c] == 1:
        memo[level][r][c] = 0
        return 0

    if level == 0:
        memo[level][r][c] = DP(0, r - 1, c) + DP(1, r - 1, c)

    elif level == 1:
        if matrix[r][c-1] == 1 or matrix[r-1][c] == 1:
            return 0
        memo[level][r][c] = DP(0, r - 1, c - 1) + DP(1, r - 1, c - 1) + DP(2, r - 1, c - 1)

    else:
        memo[level][r][c] = DP(1, r, c - 1) + DP(2, r, c - 1)

    return memo[level][r][c]


N = int(input())
dirs = [(0, 1), (1, 1), (1, 0)]
matrix = [list(map(int, input().split())) for _ in range(N)]
counter = [[0] * N for _ in range(N)]

memo = [[[0] * N for _ in range(N)] for _ in range(3)]

memo[2][0][1] = 1

print(DP(0, N - 1, N - 1) + DP(1, N - 1, N - 1) + DP(2, N - 1, N - 1))