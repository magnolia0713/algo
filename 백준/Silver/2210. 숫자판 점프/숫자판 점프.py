def dfs(depth, coord_list):

    if depth == 6:
        if a_list not in gathered_list:
            gathered_list.append(a_list.copy())
        return

    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    for i, j in vectors:
        if coord_list[0] + i < 0 or coord_list[1] + j < 0 or coord_list[0] + i > 4 or coord_list[1] + j > 4:
            continue
    
        fixed_list = [coord_list[0] + i, coord_list[1] + j]
        a_list.append(matrix[fixed_list[0]][fixed_list[1]])
        dfs(depth + 1, fixed_list)
        a_list.pop()

    return

matrix = [list(map(int, input().split())) for _ in range(5)]

gathered_list = []

for i in range(5):
    for j in range(5):
        a_list = []
        coord_list = [i, j]
        a_list.append(matrix[i][j])
        dfs(1, coord_list)

print(len(gathered_list))