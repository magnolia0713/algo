import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e9

matrix = [[[INF, 0] for _ in range(n+1)] for _ in range(n+1)]

for r in range(1,n+1):
    for c in range(1,n+1):
        if r == c:
            matrix[r][r] = [0,0]
        else:
            matrix[r][c] = [INF, [r,c]]


for _ in range(m):
    start, end, cost = map(int, input().split())

    if matrix[start][end][0] > cost:
        matrix[start][end][0] = cost






for k in range(1, n+1):
    for r in range(1, n+1):
        for c in range(1, n+1):
            if matrix[r][c][0] > matrix[r][k][0] + matrix[k][c][0]:

                matrix[r][c][0] = matrix[r][k][0] + matrix[k][c][0]
                matrix[r][c][1] = matrix[r][k][1] + matrix[k][c][1][1:]



for r in range(1, n+1):
    for c in range(1, n+1):
        if matrix[r][c][0] == INF:
            print('0', end=' ')

        else:
            print(matrix[r][c][0], end=' ')
    print()

for r in range(1, n+1):
    for c in range(1, n+1):
        if matrix[r][c][0] == 0 or matrix[r][c][0] == INF:
            print('0')

        else:
            print(len(matrix[r][c][1]), *matrix[r][c][1])