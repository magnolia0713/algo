#import time
#start_1 = time.time()
from copy import deepcopy
from collections import deque
def dfs(depth, start):
    if depth == 3:
        total_set.append(subset.copy())

    else:
        for i in range(start, len(set_list)):
            subset.append(set_list[i])
            dfs(depth+1, i+1)
            subset.pop()
#-----------------------------------------------------------------------------
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
#print(matrix)
set_list = []
subset = []
total_set = []
dirs = [[0,1], [1,0], [-1,0], [0,-1]]
# 0인 곳 부분집합 만들기
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 0:
            set_list.append([r,c])

#전염 근원지 찾기
contaminated_zone = deque()
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 2:
            contaminated_zone.append([r,c])

dfs(0,0)
maximized = 0
counter = len(set_list) - 3
for a_list in total_set:
    matrix2 = deepcopy(matrix)
    count = counter
    check_mat = [[1] * m for _ in range(n)]
    cont2 = deepcopy(contaminated_zone)

    for i, j in a_list:
        matrix2[i][j] = 1
    while cont2:
        r, c = cont2.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < m and matrix2[nr][nc] == 0 and check_mat[nr][nc] == 1:
                check_mat[nr][nc] = 0
                count -= 1
                cont2.append([nr,nc])

    if maximized < count:
        maximized = count

print(maximized)

#end_1 = time.time()
#print(end_1 - start_1)