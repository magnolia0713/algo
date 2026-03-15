from collections import deque

N, M, T = map(int, input().split())
matrix = [0] + [deque(map(int, input().split())) for _ in range(N)]

counter = N * M
for _ in range(T):

    x, d, k = map(int, input().split())

    i = 1

    while x * i <= N:
        t = x * i
        if d == 0:
            for j in range(k):
                h = matrix[t].pop()
                matrix[t].appendleft(h)

        if d == 1:
            for j in range(k):
                h = matrix[t].popleft()
                matrix[t].append(h)
        i += 1
        remover = set()


    for r in range(1,N+1):
        for c in range(M):
            if matrix[r][c] == 0:
                continue

            if matrix[r][c] == matrix[r][(c-1) % M]:
                remover |= {(r,c), (r, (c-1) % M)}

            if matrix[r][c] == matrix[r][(c+1) % M]:
                remover |= {(r,c), (r, (c+1) % M)}

            if r < N:
                if matrix[r][c] == matrix[r+1][c]:
                    remover |= {(r, c), (r+1,c)}

            if r > 1:
                if matrix[r][c] == matrix[r-1][c]:
                    remover |= {(r, c), (r-1,c)}

    counter -= len(remover)

    if remover:
        for r, c in remover:
            matrix[r][c] = 0
        
    else:
        if counter == 0:
            break
        
        else: 
            a_sum = 0
            for r in range(1,N+1):
                a_sum += sum(matrix[r])
                a_avg = a_sum / counter
    
            for r in range(1,N+1):
                for c in range(M):
                    if matrix[r][c] != 0:
                        if matrix[r][c] > a_avg:
                            matrix[r][c] -= 1
                        elif matrix[r][c] < a_avg:
                            matrix[r][c] += 1

total = 0
for r in range(1,N+1):
    total += sum(matrix[r])

print(total)