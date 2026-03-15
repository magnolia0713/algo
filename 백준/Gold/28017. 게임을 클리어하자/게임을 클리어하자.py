n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

memo = [[0] * m for _ in range(n)]

for c in range(m):
    memo[0][c] = matrix[0][c]

for r in range(1, n):
    left_min = [0] * m
    right_min = [0] * m

    left_min[0] = memo[r-1][0]
    for c in range(1, m):
        left_min[c] = min(left_min[c-1], memo[r-1][c])

    right_min[m-1] = memo[r-1][m-1]
    for c in range(m-2, -1, -1):
        right_min[c] = min(right_min[c+1], memo[r-1][c])

    for c in range(m):
        if c == 0:
            best_prev = right_min[1]
        elif c == m - 1:
            best_prev = left_min[m - 2]
        else:
            best_prev = min(left_min[c - 1], right_min[c + 1])

        memo[r][c] = matrix[r][c] + best_prev

print(min(memo[n - 1]))
