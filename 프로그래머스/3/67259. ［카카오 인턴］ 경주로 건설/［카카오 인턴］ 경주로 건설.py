from heapq import heappush, heappop

def solution(board):
    n = len(board)
    inf = 1e9

    # answer_sheet[방향][행][열]
    # 0: 위, 1: 왼쪽, 2: 아래, 3: 오른쪽
    answer_sheet = [[[inf] * n for _ in range(n)]for _ in range(4)]

    unit_vector = [
        (-1, 0),  # 위
        (0, -1),  # 왼쪽
        (1, 0),   # 아래
        (0, 1)    # 오른쪽
    ]

    # 시작점에서는 오른쪽 또는 아래로 출발 가능
    answer_sheet[2][0][0] = 0
    answer_sheet[3][0][0] = 0

    basket = [ (0, 0, 0, 2), (0, 0, 0, 3)]

    while basket:
        weight, r, c, dirr = heappop(basket)

        # 이미 더 저렴한 경로가 있으면 무시
        if weight > answer_sheet[dirr][r][c]:
            continue

        for i in range(4):

            # 같은 방향
            if i == dirr:
                cost = 100

            # 반대 방향
            elif i % 2 == dirr % 2:
                continue

            # 90도 회전
            else:
                cost = 600

            dr, dc = unit_vector[i]
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n and 0 <= nc < n):
                continue

            if board[nr][nc] == 1:
                continue

            new_cost = weight + cost

            if new_cost < answer_sheet[i][nr][nc]:
                answer_sheet[i][nr][nc] = new_cost
                heappush(basket, (new_cost, nr, nc, i))

    return min(answer_sheet[i][n - 1][n - 1] for i in range(4))