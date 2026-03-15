def find_subset(depth, start):
    if depth == m:
        total_list.append(subset_list.copy())
    else:
        for i in range(start, len(chicken_house)):
            subset_list.append(chicken_house[i].copy())
            find_subset(depth+1, i+1)
            subset_list.pop()

#-----------------------------------------------------------------------------

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

#print(matrix)
chicken_house = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 2:
            chicken_house.append([r,c])

#print(chicken_house)

subset_list = []
total_list = []

find_subset(0,0)
#print(total_list)
total_min = 250000
for a_list in total_list:
    #print(a_list)
    mini_sum = 0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 1:
                min_a = 100
                for lr, lc in a_list:
                    #print(r, c, lr, lc)
                    if min_a > abs(r - lr) + abs(c - lc):
                        min_a = abs(r - lr) + abs(c - lc)
                    #print(min_a)
                mini_sum += min_a
    if total_min > mini_sum:
        total_min = mini_sum

print(total_min)