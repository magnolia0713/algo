def subseting(start=0, depth=0,cnt_y=0):
    global total_count
    if cnt_y == 4:
        return

    if depth < 7:
        for i in range(start,25):
            if matrix[total_subset[i][0]][total_subset[i][1]] == 'Y':
                subset.append(total_subset[i])
                subseting(i+1,depth+1,cnt_y+1)
                subset.pop()
            else:
                subset.append(total_subset[i])
                subseting(i+1,depth+1,cnt_y)
                subset.pop()


    else:
        basket = [tuple(subset[0])]
        count_a = 1
        check_list = [tuple(subset[0])]
        while basket:
            n, m = basket.pop()
            for dr, dc in dirs:
                nr = n + dr
                nc = m + dc
                if (nr,nc) in subset and (nr, nc) not in check_list:
                    basket.append((nr,nc))
                    check_list.append((nr,nc))
                    count_a += 1

            if count_a == 7:
                total_count += 1
                break


#=================================================
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
matrix = [list(input()) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
total_count = 0
total_subset = [(i,j) for i in range(5) for j in range(5)]
subset = []
count = cnt_y = 0
subseting()
print(total_count)
