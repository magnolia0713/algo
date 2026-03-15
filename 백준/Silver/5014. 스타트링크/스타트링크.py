# import time
# start_a = time.time()
from collections import deque
def bfs(start):
    stack = deque([start])

    while stack:
        floor_a = stack.popleft()
        if floor_a == G:
            return distance[G]

        for dr in dirs:
            nr = floor_a + dr
            if 1 <= nr <= F and distance[nr] == -1:
                distance[nr] = distance[floor_a] + 1
                stack.append(nr)

    return 'use the stairs'
#========================
F, S, G, U ,D = map(int, input().split())
dirs = [U,-D]
distance = [-1] * (F+1) # 거리와 visited 동시처리, 한칸 +해서 인덱스 맞추기
distance[S] = 0
print(bfs(S))

# end_a = time.time()
# print(end_a - start_a)