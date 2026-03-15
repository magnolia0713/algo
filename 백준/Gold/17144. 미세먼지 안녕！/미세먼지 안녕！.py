import sys
# import time
# start_time =time.time()
input = sys.stdin.readline
R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
dirs = [(0,1), (0,-1),(1,0),(-1,0)]
for i in range(R):
    if matrix[i][0] == -1:
        cleaner = [i, i+1]
        break
counter = 0

for _ in range(T):
    matrix2 = [[0] * C for _ in range(R)]
    matrix2[cleaner[0]][0] = -1
    matrix2[cleaner[1]][0] = -1
    for r in range(R):
        for c in range(C):
            if r not in cleaner or c != 0:
                matrix2[r][c] += matrix[r][c]
                spreading = matrix[r][c] // 5
                if spreading:
                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < R and 0 <= nc < C:
                            if nr not in cleaner or nc != 0:
                                matrix2[nr][nc] += spreading
                                matrix2[r][c] -= spreading

    matrix = matrix2
    #1
    for r in range(cleaner[0], -1, -1):
        matrix2[r+1][0] = matrix2[r][0]
    matrix2[cleaner[0]][0] = -1
    for r in range(cleaner[0] + 1, R):
        matrix2[r-1][0] = matrix2[r][0]
    matrix2[cleaner[1]][0] = -1

    #2
    for c in range(1,C):
        matrix2[0][c-1] = matrix2[0][c]
        matrix2[R-1][c-1] = matrix2[R-1][c]

    #3
    for r in range(1, cleaner[0]+1):
        matrix2[r-1][C-1] = matrix2[r][C-1]
    for r in range(R-1, cleaner[1], -1):
        matrix2[r][C-1] = matrix2[r-1][C-1]

    #4
    for c in range(C-2, 0, -1):
        matrix2[cleaner[0]][c+1] = matrix2[cleaner[0]][c]
        matrix2[cleaner[1]][c+1] = matrix2[cleaner[1]][c]
    matrix2[cleaner[0]][1] = matrix2[cleaner[1]][1] = 0


total_a = 0
for i in matrix2:
    total_a += sum(i)

print(total_a+2)

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"코드 실행 시간: {execution_time} 초")