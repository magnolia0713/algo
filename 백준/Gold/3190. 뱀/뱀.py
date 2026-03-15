from collections import deque

def lifetime():
    global dir, head_r, head_c
    time = 0



    while True:
        
        time += 1
        # 방향 전환
        if order:
            if order[0][0]+1 == time:
                p, q = order.popleft()
                if q == 'L':
                    dir -= 1
                else:
                    dir += 1

        #머리 늘리기
        head_r += dir_r[dir%4] ; head_c += dir_c[dir%4]
        if head_r >= N or head_c >= N or head_c < 0 or head_r < 0:
            return time

        if matrix[head_r][head_c] == 0:
            matrix[head_r][head_c] = 1
            basket.append((head_r, head_c))

        elif matrix[head_r][head_c] == 1:
            return time

        else:
            matrix[head_r][head_c] = 1
            basket.append((head_r, head_c))
            continue

        x, y = basket.popleft()
        matrix[x][y] = 0



N = int(input()) #행렬크기

K = int(input()) # 사과의 수

matrix = [[0] * N for _ in range(N)]
matrix[0][0] = 1
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
dir = 0
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 2

L = int(input())
order = deque()
for _ in range(L):
    i, j = input().split()
    i = int(i)
    order.append([i,j])
head_r = head_c = 0
tail_r = tail_c = 0

basket = deque([(0,0)])
result = lifetime()
print(result)