from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix_a = [list(map(int, list(input().strip()))) for _ in range(N)]
cube = []
for _ in range(N):
    matrix = []
    for _ in range(M):
        list_a = []
        for _ in range(2):
            list_a.append(0)
        matrix.append(list_a)
    cube.append(matrix)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
basket = deque([(0,0,1)])
cube[0][0][1] = 1
check = False
while basket:
    n, m, coin = basket.popleft()
    if n == N-1 and m == M-1:
        print(cube[n][m][coin])
        break

    for dr, dc in dirs:
        nn = n + dr
        nm = m + dc
        if 0 <= nn < N and 0 <= nm < M:
            if matrix_a[nn][nm] == 0 and cube[nn][nm][coin] == 0:
                cube[nn][nm][coin] = cube[n][m][coin] + 1
                basket.append((nn,nm,coin))
            elif coin and matrix_a[nn][nm] == 1 and cube[nn][nm][coin-1] == 0:
                cube[nn][nm][coin-1] = cube[n][m][coin] + 1
                basket.append((nn,nm,coin-1))

else:
    print(-1)