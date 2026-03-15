n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
INF = 111111

memo1 = [[-INF] * m for _ in range(n)]
memo2 = [[-INF] * m for _ in range(n)]

memo1[0][0] = matrix[0][0]
memo2[0][0] = matrix[0][0]

for i in range(m-1):
    memo1[0][i+1] = memo1[0][i] + matrix[0][i+1]

for r in range(1,n):
    memo1[r][0] = memo1[r-1][0] + matrix[r][0]
    memo2[r][m-1] = memo1[r-1][m-1] + matrix[r][m-1]
    
    for c in range(m-1):
        memo1[r][c+1] = max(memo1[r-1][c+1], memo1[r][c]) + matrix[r][c+1]
        memo2[r][m - (c+2)] = max(memo1[r-1][m - (c+2)], memo2[r][m - (c+1)]) + matrix[r][m - (c+2)]

    for c in range(m):
        memo1[r][c] = max(memo1[r][c], memo2[r][c])


print(memo1[n-1][m-1])