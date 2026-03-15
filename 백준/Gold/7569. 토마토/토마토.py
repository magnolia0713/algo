import sys
M, N, H = map(int, input().split())
box = []
for _ in range(H):
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    box.append(matrix)

dir = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0),(0,0,1), (0,0,-1)]
basket = []
basket2 = []
count_z = 0
counter = 0
first = True

while True:
    if first:
        for h in range(H):
            for r in range(N):
                for c in range(M):
                    if box[h][r][c] == 1:
                        basket.append((h, r, c))

    if not basket2 and not first:
        for h in box:
            for r in h:
                count_z += r.count(0)
        if count_z == 0:
            print(counter - 1)
            break
        else:
            print(-1)
            break

    while basket2 or first:
        if first:
            if not basket:
                first = False
                break
            basket2 = basket.copy()
            basket.clear()
            first = False

        h, r, c = basket2.pop()
        for dh, dr, dc in dir:
            nh = h + dh
            nr = r + dr
            nc = c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and box[nh][nr][nc] == 0:
                box[nh][nr][nc] = 1
                basket.append((nh, nr, nc))

    basket2 = basket.copy()
    basket.clear()
    counter += 1