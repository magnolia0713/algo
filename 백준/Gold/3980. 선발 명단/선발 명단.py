def optimize(depth=0):
    global sum_max


    if depth == 11:
        if sum_max < sum(sum_a):
            sum_max = sum(sum_a)
        return

    for j in range(11):
        if matrix[depth][j] != 0 and checker_po[j] == 0:
            sum_a.append(matrix[depth][j])
            checker_po[j] = 1

            optimize(depth + 1)

            checker_po[j] = 0
            sum_a.pop()

T = int(input())
for t in range(T):

    matrix = [list(map(int, input().split())) for _ in range(11)]
    
    checker_po = [0] * 11
    checker_player = [0] * 11
    sum_a = []
    sum_max = 0
    
    optimize(0)

    print(sum_max)