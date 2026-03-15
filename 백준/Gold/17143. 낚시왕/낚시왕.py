def catch():
    for i in range(R):
        if data_org[i][idx]:
            result = data_org[i][idx][2]
            data_org[i][idx] = 0
            break
    else:
        result = 0
    return result


def shark_move():
    data = [row[:] for row in matrix]

    for p in range(R):
        for q in range(C):
            if data_org[p][q]:
                s, d, z = data_org[p][q]

                r = p
                c = q
                nd = d

                if d == 0 or d == 2:
                    period = 2 * (C - 1)
                    if period == 0:
                        nr, nc, nd = r, c, d
                    else:
                        step = s if d == 0 else -s
                        t = (c + step) % period
                        if t >= C:
                            nc = 2 * (C - 1) - t
                            nd = 2 - d
                        else:
                            nc = t
                            nd = d
                        nr = r
                else:
                    period = 2 * (R - 1)
                    if period == 0:
                        nr, nc, nd = r, c, d
                    else:
                        step = s if d == 1 else -s
                        t = (r + step) % period
                        if t >= R:
                            nr = 2 * (R - 1) - t
                            nd = 4 - d
                        else:
                            nr = t
                            nd = d
                        nc = c

                if data[nr][nc]:
                    if data[nr][nc][2] < z:
                        data[nr][nc] = (s, nd, z)
                else:
                    data[nr][nc] = (s, nd, z)

    return data


R, C, M = map(int, input().split())

matrix = [[0] * C for _ in range(R)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
idx = 0
fish_list = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())

    if d == 1:
        d = 3
        p = 0 if R == 1 else (s % (2 * R - 2))
    elif d == 2:
        d = 1
        p = 0 if R == 1 else (s % (2 * R - 2))
    elif d == 3:
        d = 0
        p = 0 if C == 1 else (s % (2 * C - 2))
    else:
        d = 2
        p = 0 if C == 1 else (s % (2 * C - 2))

    fish_list.append((r - 1, c - 1, p, d, z))

data_org = [[0] * C for _ in range(R)]
for r, c, p, d, z in fish_list:
    data_org[r][c] = (p, d, z)


idx = 0
cnt = 0

while idx < C:
    cnt += catch()
    idx += 1
    data_org = shark_move()
    
    # for i in data_org:
    #     print(*i)
    # print()

print(cnt)