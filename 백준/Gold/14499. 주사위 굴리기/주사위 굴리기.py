from collections import deque
N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

order = list(map(int, input().split()))
dir_x = [0, 0, 0, -1, 1]
dir_y = [0,1, -1, 0, 0]
dice = [0,0,0,0,0,0]
ans_list = []

for i in order:
    nx = x + dir_x[i]
    ny = y + dir_y[i]
    if nx >= N or ny >= M or nx < 0 or ny < 0:
        continue

    else:
        x, y = nx, ny
        if i == 1:
            dice = [dice[0],dice[2],dice[3],dice[5],dice[4],dice[1]]

        elif i == 2:
            dice = [dice[0],dice[5],dice[1],dice[2],dice[4],dice[3]]

        elif i == 3:
            dice = [dice[5],dice[1],dice[0],dice[3],dice[2],dice[4]]

        else:
            dice = [dice[2],dice[1],dice[4],dice[3],dice[5],dice[0]]

    if matrix[x][y] == 0:
        matrix[x][y] = dice[2]
    else:
        dice[2] = matrix[x][y]
        matrix[x][y] = 0

    ans_list.append(str(dice[5]))
print('\n'.join(ans_list))