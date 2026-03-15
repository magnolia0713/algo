T = int(input())

map_list = list(map(int, input().split()))

total_hill = 0

hill = 0

for i in range(T-1):
    if map_list[i] < map_list[i+1]:
        hill += map_list[i+1] - map_list[i]
        if hill >= total_hill:
            total_hill = hill
    else:
        if hill >= total_hill:
            total_hill = hill
        hill = 0


print(total_hill)