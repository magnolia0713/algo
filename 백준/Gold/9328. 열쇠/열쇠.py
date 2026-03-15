from collections import deque
from collections import defaultdict

t = int(input())

def bfs():

    cnt = 0
    visited = [[0] * c for _ in range(r)]
    key_dict = [[] for _ in range(130)]
    keys = input()
    if keys != '0':
        for i in keys:
            key_dict[ord(i)] = 1

    room_dict = defaultdict(list)

    while basket:
        p, q = basket.popleft()

        for dp, dq in dirs:
            np = p + dp
            nq = q + dq

            if 0 <= np < r and 0 <= nq < c and not visited[np][nq]:

                #통로
                if matrix[np][nq] == '.':
                    visited[np][nq] = 1
                    basket.append((np, nq))

                #소문자
                elif 97 <= ord(matrix[np][nq]) <= 122:
                    key_dict[ord(matrix[np][nq])] = 1
                    visited[np][nq] = 1
                    basket.append((np, nq))

                    if room_dict[ord(matrix[np][nq]) - 32]:
                        for a, b in room_dict[ord(matrix[np][nq]) - 32]:
                            if not visited[a][b]:
                                basket.append((a, b))

                #대문자
                elif 65 <= ord(matrix[np][nq]) <= 90:
                    if key_dict[ord(matrix[np][nq]) + 32]:
                        basket.append((np,nq))
                        visited[np][nq] = 1


                    else:
                        room_dict[ord(matrix[np][nq])].append((np, nq))

                elif matrix[np][nq] == '$':
                    visited[np][nq] = 1
                    basket.append((np, nq))
                    cnt += 1


    # for i in visited:
    #     print(*i)

    return cnt




dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for tc in range(t):

    r, c = map(int, input().split())
    matrix = [list(input()) for _ in range(r)]

    basket = deque()

    for i in range(r):
        basket.append((i, -1))
        basket.append((i, c))

    for j in range(1, c-1):
        basket.append((-1, j))
        basket.append((r, j))


    result = bfs()
    print(result)

