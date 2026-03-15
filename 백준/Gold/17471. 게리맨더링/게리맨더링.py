from collections import deque

def bfs(sub_list):
    basket = deque([sub_list[0]])
    storage = [sub_list[0]]
    while basket:
        num = basket.popleft()
        for i in neighbor_list[num]:
            if i in neighbor_list[num] and i not in storage and i in sub_list:
                basket.append(i)
                storage.append(i)

    if len(storage) == len(sub_list):
        return True
    else:
        return False

N = int(input())
subset_list = []
set_list = list(range(1,N+1))
popul_list = list(map(int, input().split()))
popul_list.insert(0,[0])
neighbor_list  =[[0]]
total_min = 1000
for i in range(1, N+1):
    neighbor_list.append(list(map(int, input().split()))[1:])

for i in range(1, (1<<N)-1):
    subset = []

    for j in range(N):
        if i & (1<<j):
            subset.append(set_list[j])
    subset_list.append(subset)


for a_list in subset_list:
    b_list = subset_list.pop()

    if bfs(a_list) and bfs(b_list):
        sum_a = 0
        for i in a_list:
            sum_a += popul_list[i]

        sum_b = 0
        for i in b_list:
            sum_b += popul_list[i]

        if total_min > abs(sum_a - sum_b):
            total_min = abs(sum_a - sum_b)

if total_min == 1000:
    total_min = -1
print(total_min)