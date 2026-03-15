def dfs(depth, matrix):
    # 1인 지점 찾기
    global a_min, end_mark

    if end_mark:
        return

    check = False
    for r in range(10):
        if check:
            break

        for c in range(10):
            if matrix[r][c] == 1:
                check = True
                n,m = r,c
                break

    #전부다 매꿨으면 리턴.
    if not check:
        if a_min > depth:
            a_min = depth

        if a_min == (total_value - 1) // 25 + 1:
            end_mark = True
        return


    #색종이 5부터 붙이기
    for i in range(4,-1,-1):
        if papers[i]:
            flag = False

            #i크기 색종이 맞는지 확인
            if n + i < 10 and m + i < 10:
                for p in range(n, n+i+1):
                    if flag:
                        break
                    for q in range(m, m+i+1):
                        if matrix[p][q] == 0:
                            flag = True
                            break

                if not flag:
                    papers[i] -= 1
                    data = [matrix[i][:] for i in range(10)]
                    for p in range(n, n+i+1):
                        for q in range(m, m+i+1):
                            data[p][q] = 0
                    dfs(depth+1, data)
                    papers[i] += 1


papers = [5,5,5,5,5]
matrix = [list(map(int, input().split())) for _ in range(10)]
a_min = 26

total_value = 0
for r in range(10):
    total_value += sum(matrix[r])

end_mark = False

dfs(0,matrix)
if a_min == 26:
    a_min = -1
print(a_min)