from collections import deque
from itertools import combinations

def land(r,c):
    lands = [(r,c)]
    basket = deque([(r,c)])
    visited[r][c] = 1
    while basket:
        p, q = basket.popleft()
        for i in range(4):
            np = p + dir_r[i]
            nq = q + dir_c[i]

            if 0 <= np < N and 0 <= nq < M and matrix[np][nq] and not visited[np][nq]:
                visited[np][nq] = 1
                basket.append((np,nq))
                lands.append((np,nq))

    total_land.append(lands)

def checking():
    basket = [0]
    full_count = {0}
    while basket:
        t = basket.pop()
        for u in mini_linked[t]:
            if u not in full_count:
                full_count.add(u)
                basket.append(u)

    if len(full_count) == len(total_land):
        return True

    else:
        return False



total_land = []
dir_r = [1,-1,0,0]
dir_c = [0,0,1,-1]
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1 and not visited[r][c]:
            land(r,c)

linked_dict = {}
linked_list = [[] for _ in range(len(total_land))]

for i in range(len(total_land)):
    for j in range(i+1, len(total_land)):
        for a, b in total_land[i]:
            for c,d in total_land[j]:
                if a == c:
                    temp = abs(b - d) - 1
                    if temp == 1:
                        continue

                    if b < d:
                        e,f = b,d
                    else:
                        e,f = d,b

                    check = False

                    for x in range(e+1,f):
                        if matrix[a][x] == 1:
                            check = True

                    if check:
                        continue

                    if (i, j) in linked_dict:
                        if linked_dict[(i, j)] > temp:
                            linked_dict[(i, j)] = temp
                    else:
                        linked_dict[(i, j)] = temp
                        linked_list[i].append(j)
                        linked_list[j].append(i)


                if b == d:

                    temp = abs(a - c) - 1

                    if temp == 1:
                        continue

                    if a < c:
                        e, f = a, c
                    else:
                        e, f = c, a

                    check = False

                    for x in range(e + 1, f):
                        if matrix[x][b] == 1:
                            check = True

                    if check:
                        continue


                    if (i,j) in linked_dict:
                        if linked_dict[(i,j)] > temp:
                            linked_dict[(i,j)] = temp
                    else:
                        linked_dict[(i,j)] = temp
                        linked_list[i].append(j)
                        linked_list[j].append(i)


subsets = list(combinations(linked_dict, len(total_land)- 1))
total_min = 999
for subset in subsets:
    mini_sum = 0
    mini_linked = [[] for _ in range(len(total_land))]

    for sub in subset:
        mini_sum += linked_dict[sub]
        mini_linked[sub[0]].append(sub[1])
        mini_linked[sub[1]].append(sub[0])

    if total_min <= mini_sum:
        continue

    else:
        if checking():
            total_min = mini_sum
if total_min == 999:
    total_min = -1
print(total_min)