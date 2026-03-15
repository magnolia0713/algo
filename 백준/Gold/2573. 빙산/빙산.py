import sys
input = sys.stdin.readline

def bfs():
    global day
    global land_list
    while True:
        day += 1
        land_list = set(land_list)
        for p, q in melted_list:
            matrix[p][q] = 0

        land_list -= melted_list
        land_list = list(land_list)
        melted_list.clear()
        #
        # for i in matrix:
        #     print(*i)
        # print()
        if not land_list:
            return 0
        if checking():
            return day


        for r, c in land_list:
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if matrix[nr][nc] == 0:       #nr과 nc의 영역체크를 할 이유가 없음, 바깥은 항상 0이기 때문
                    matrix[r][c] -= 1
                    if matrix[r][c] == 0:
                        matrix[r][c] = -1
                        melted_list.add((r,c))
                        break

def checking():
    count = 1
    basket = [land_list[0]]
    daily_check = {land_list[0]}
    while basket:
        n, m = basket.pop()
        for dn, dm in dirs:
            nn = n + dn
            nm = m + dm
            if matrix[nn][nm] != 0 and (nn,nm) not in daily_check:
                count += 1
                basket.append((nn,nm))
                daily_check.add((nn,nm))

    if count == len(land_list):
        return False
    else:
        return True
#=================================================================
dirs = [[0,1],[1,0],[-1,0],[0,-1]]
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
land_list = []
melted_list = set()
for r in range(N):
    for c in range(M):
        if matrix[r][c] != 0:
            land_list.append((r,c))

day = -1
print(bfs())