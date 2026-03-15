def dp(depth, color):
    if depth == 1:
        return matrix[1][color]

    else:
        if dp_mat[depth][color] != 0:
            return dp_mat[depth][color]

        else:
            dp_mat[depth][color] = min(dp(depth-1, (color+1)%3), dp(depth-1, (color+2)%3)) + matrix[depth][color]
            return dp_mat[depth][color]

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
matrix.insert(0,[0,0,0])
dp_mat = [[0]*3 for _ in range(n+1)]
for i in range(3):
    dp_mat[1][i] = matrix[1][i]

print(min(dp(n,0), dp(n,1), dp(n,2)))