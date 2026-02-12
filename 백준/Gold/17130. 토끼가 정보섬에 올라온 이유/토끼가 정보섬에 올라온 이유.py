
n, m = map(int, input().split())


# 매트릭스에서 한 쪽으로 이동, 입력 최대값이 DP로 추정하게 함
# => bottom up dp
matrix = [list(input()) for _ in range(n)]
dp_carrot = [[0] * m for _ in range(n)]
#토끼 찾기
rabbit = 0
for c in range(m):
    for r in range(n):
        if matrix[r][c] == 'R':
            rabbit = (r,c)

    if rabbit:
        break
# 1로 표시해서 true/false를 구분하고 최종 결과값에 -1을 해준다.
dp_carrot[rabbit[0]][rabbit[1]] = 1
max_carrot = -1
# 당근 찾기

# r이 한 줄일 때
if n == 1:
    for c in range(rabbit[0]+1, m):
        if matrix[0][c] == 'C':
            dp_carrot[0][c] = dp_carrot[0][c-1]
            if dp_carrot[0][c] >= 1:
                dp_carrot[0][c] += 1

        elif matrix[0][c] == '.':
            dp_carrot[0][c] = dp_carrot[0][c-1]

        elif matrix[0][c] == 'O':
            dp_carrot[0][c] = dp_carrot[0][c-1]
            max_carrot = max(max_carrot, dp_carrot[0][c] - 1)


else:
    for c in range(rabbit[1]+1, m):
        for r in range(n):
            if 0 < r < n-1:
                if matrix[r][c] == 'C':
                    dp_carrot[r][c] = max(dp_carrot[r-1][c-1], dp_carrot[r][c-1], dp_carrot[r+1][c-1])
                    if dp_carrot[r][c] >= 1:
                        dp_carrot[r][c] += 1

                elif matrix[r][c] == '.':
                    dp_carrot[r][c] = max(dp_carrot[r-1][c-1], dp_carrot[r][c-1], dp_carrot[r+1][c-1])

                elif matrix[r][c] == 'O':
                    dp_carrot[r][c] = max(dp_carrot[r-1][c-1], dp_carrot[r][c-1], dp_carrot[r+1][c-1])
                    max_carrot = max(max_carrot, dp_carrot[r][c] - 1)

            elif r == 0:
                if matrix[r][c] == 'C':
                    dp_carrot[r][c] = max(dp_carrot[r][c-1], dp_carrot[r+1][c-1])
                    if dp_carrot[r][c] >= 1:
                        dp_carrot[r][c] += 1

                elif matrix[r][c] == '.':
                    dp_carrot[r][c] = max(dp_carrot[r][c-1], dp_carrot[r+1][c-1])

                elif matrix[r][c] == 'O':
                    dp_carrot[r][c] = max(dp_carrot[r][c-1], dp_carrot[r+1][c-1])
                    max_carrot = max(max_carrot, dp_carrot[r][c] - 1)
            elif r == n-1:
                if matrix[r][c] == 'C':
                    dp_carrot[r][c] = max(dp_carrot[r-1][c-1], dp_carrot[r][c-1])
                    if dp_carrot[r][c] >= 1:
                        dp_carrot[r][c] += 1

                elif matrix[r][c] == '.':
                    dp_carrot[r][c] = max(dp_carrot[r-1][c-1], dp_carrot[r][c-1])

                elif matrix[r][c] == 'O':
                    dp_carrot[r][c] = max(dp_carrot[r-1][c-1], dp_carrot[r][c-1])
                    max_carrot = max(max_carrot, dp_carrot[r][c] - 1)

print(max_carrot)