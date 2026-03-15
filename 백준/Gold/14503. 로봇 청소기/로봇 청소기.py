def robot_cleaning(n,m,dir):
    if check_mat[n][m] == 0:
        check_mat[n][m] = 1
        counter[0] += 1

    for num in range(1,5):
        dir -= 1
        nn = n + dirs[dir % 4][0]
        nm = m + dirs[dir % 4][1]
        #print(nn, nm,matrix[nn][nm], check_mat[nn][nm])
        if 0 <= nn < N and 0 <= nm < M and not matrix[nn][nm] and not check_mat[nn][nm]:
            #print('check')
            robot_cleaning(nn,nm,dir)
            return

    else:
        if matrix[n - dirs[dir % 4][0]][m - dirs[dir % 4][1]] == 0:
            robot_cleaning(n - dirs[dir % 4][0], m - dirs[dir % 4][1], dir)
            return
        else:
            return



#---------------------------------------

N, M = map(int, input().split())
n, m, dir = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

check_mat = [[0] * M for _ in range(N)]
dirs = [(-1,0), (0,1), (1,0),(0,-1)]
counter = [0]
robot_cleaning(n, m, dir)
print(counter[0])