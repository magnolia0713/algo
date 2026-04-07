# 데스 나이트

# bfs로 가능할 듯 싶다.
from collections import deque

n = int(input())
sr, sc, er, ec = map(int, input().split())

def bfs(sr, sc):
    movement = [(-2, -1), (-2, +1), (0, -2), (0, +2), (+2, -1), (+2, +1)]
    basket = deque(); basket.append((sr, sc))
    visited = [[0] * n for _ in range(n)]; visited[sr][sc] = 1

    while basket:
        r, c = basket.popleft()
        for dr, dc in movement:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if nr == er and nc == ec:
                    return visited[r][c] + 1
                visited[nr][nc] = visited[r][c] + 1
                basket.append((nr, nc))
    return 0

ans = bfs(sr, sc) - 1
print(ans)
