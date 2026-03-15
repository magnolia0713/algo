N, M = map(int, input().split())

matrix_chess = list(list(input()) for _ in range(N))

min_a = 64

for k in range(0,N - 7):
    for l in range(0, M - 7):
        count_a = 0

        for i in range(k,k+8):
            for j in range(l,l+8):
                if (i + j) % 2 == 0:
                    if matrix_chess[i][j] == 'W':
                        count_a += 1
                else:
                    if matrix_chess[i][j] == 'B':
                        count_a += 1

        if count_a > 32 :
            count_a = 64 - count_a

        if count_a < min_a:
            min_a = count_a



print(min_a)