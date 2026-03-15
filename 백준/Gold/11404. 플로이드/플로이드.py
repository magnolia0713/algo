import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e9
matrix = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    matrix[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    if matrix[start][end] > cost:
        matrix[start][end] = cost

for k in range(1, n+1):
    for r in range(1, n+1):
        for c in range(1, n+1):
            matrix[r][c] = min(matrix[r][c], matrix[r][k] + matrix[k][c])

for r in range(1, n+1):
    for c in range(1, n+1):
        if matrix[r][c] == INF:
            print('0', end=' ')

        else:
            print(matrix[r][c], end=' ')

    print()