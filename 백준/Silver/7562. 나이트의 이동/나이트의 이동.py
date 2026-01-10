from collections import deque

def bfs(start, end):
    basket = deque([start])
    distance[start[0]][start[1]] = 0

    while basket:
        n, m = basket.popleft()
        for dr, dc in dirs:
            nr = n + dr
            nc = m + dc
            if 0 <= nr < N and 0 <= nc < N and distance[nr][nc] == -1:
                distance[nr][nc] = distance[n][m] + 1
                basket.append([nr,nc])
                if nr == end[0] and nc == end[1]:
                    return distance[nr][nc]
#----------------------------------------------------------------------


dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

T = int(input())
for _ in range(T):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    if start == end:
        print(0)
        continue

    distance = [[-1] * N for _ in range(N)]

    result = bfs(start, end)
    print(result)