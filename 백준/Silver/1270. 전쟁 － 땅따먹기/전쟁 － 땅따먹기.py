from collections import defaultdict
n = int(input())
ans_list = []

for _ in range(n):
    a_dict = defaultdict(int)
    n_list = list(map(int, input().split()))
    num = n_list[0]

    for i in range(1, num+1):
        a_dict[n_list[i]] += 1


    for idx, size in a_dict.items():
        if size > num//2:
            ans_list.append(idx)
            break
    else:
        ans_list.append('SYJKGW')

print(*ans_list, sep='\n')