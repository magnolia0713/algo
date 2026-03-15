
from collections import deque

def bfs():

    p_basket = deque([person])
    f_basket = deque(fire)
    cnt = 0

    while p_basket:

        cnt += 1

        for _ in range(len(f_basket)):

            p, q = f_basket.popleft()
            for dp, dq in dirs:
                np = p + dp
                nq = q + dq

                if 0 <= np < r and 0 <= nq < c and (matrix[np][nq] == '.' or matrix[np][nq] == 'J'):
                    f_basket.append((np,nq))
                    matrix[np][nq] = 'F'

        for _ in range(len(p_basket)):
            p, q = p_basket.popleft()
            for dp, dq in dirs:
                np = p + dp
                nq = q + dq

                if 0 <= np < r and 0 <= nq < c:
                    if matrix[np][nq] == '.':
                        p_basket.append((np,nq))
                        matrix[np][nq] = 'J'

                else:
                    return cnt

    return 'IMPOSSIBLE'

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]

fire = []
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'F':
            fire.append((i,j))

        elif matrix[i][j] == 'J':
            person = (i,j)

print(bfs())