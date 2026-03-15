from collections import deque
N = int(input())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
while True:
    mem_a, mem_b = map(int, input().split())
    if mem_a == mem_b == -1:
        break
    matrix[mem_a][mem_b] = matrix[mem_b][mem_a] = 1

#print(matrix)

def bfs(member, depth):

    if len(member_set) == N:
        list_final[member] = depth
        return

    len_a = len(basket)
    for _ in range(len_a):
        mem_num = basket.popleft()
        for idx in range(len(matrix[mem_num])):
            if matrix[mem_num][idx] == 1:
                member_set.add(idx)
                basket.append(idx)
                member_set.add(idx)
    bfs(member, depth+1)

list_final = [0] * (N+1)
for member in range(1, N+1):
    member_set = {member}
    basket = deque()
    basket.append(member)
    result = bfs(member, 0)

min_a = list_final[1]
for i in list_final:
    if min_a > i and i != 0:
        min_a = i
print(min_a, list_final.count(min_a))
for j in range(len(list_final)):
    if min_a == list_final[j]:
        print(j, end=' ')