def bfs():
    global max_a

    for r in range(N):
        for c in range(M):
            for tetros in totals:
                mini_sum = 0
                for dr, dc in tetros:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M:
                        mini_sum += matrix[nr][nc]
                    else:
                        break

                if max_a < mini_sum:
                    max_a = mini_sum

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_a = 0

#네모
tetro_dir0_a = [(0,0),(1,0),(0,1),(1,1)]

#그 긴거

tetro_dir1_a = [(0,0),(1,0),(2,0),(3,0)]
tetro_dir1_b = [(0,0),(0,1),(0,2),(0,3)]

#볼록할철
tetro_dir2_a = [(0,0),(1,0),(-1,0),(0,1)]
tetro_dir2_b = [(0,0),(1,0),(-1,0),(0,-1)]
tetro_dir2_c = [(0,0),(1,0),(0,1),(0,-1)]
tetro_dir2_d = [(0,0),(-1,0),(0,1),(0,-1)]

#번개모양
tetro_dir3_a = [(0,0),(1,0),(1,1),(2,1)]
tetro_dir3_b = [(0,0),(1,0),(1,-1),(2,-1)]
tetro_dir3_c = [(0,0),(0,1),(1,1),(1,2)]
tetro_dir3_d = [(0,0),(0,1),(-1,1),(-1,2)]

#L
tetro_dir4_a = [(0,0),(1,0),(2,0),(2,1)]
tetro_dir4_b = [(0,0),(1,0),(2,0),(2,-1)]
tetro_dir4_c = [(0,0),(0,1),(0,2),(1,2)]
tetro_dir4_d = [(0,0),(0,1),(0,2),(-1,2)]
tetro_dir4_e = [(0,0),(-1,0),(-2,0),(-2,1)]
tetro_dir4_f = [(0,0),(-1,0),(-2,0),(-2,-1)]
tetro_dir4_g = [(0,0),(0,-1),(0,-2),(1,-2)]
tetro_dir4_h = [(0,0),(0,-1),(0,-2),(-1,-2)]

totals = [tetro_dir0_a, tetro_dir1_a, tetro_dir1_b, tetro_dir2_a, tetro_dir2_b, tetro_dir2_c, tetro_dir2_d, tetro_dir3_a, tetro_dir3_b, tetro_dir3_c, tetro_dir3_d, tetro_dir4_a, tetro_dir4_b, tetro_dir4_c, tetro_dir4_d, tetro_dir4_e, tetro_dir4_f, tetro_dir4_g, tetro_dir4_h]
bfs()
print(max_a)