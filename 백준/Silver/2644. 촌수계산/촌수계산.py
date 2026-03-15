from collections import deque
def bfs(start):
    stack = deque([start])
    count = 0
    while stack:
        mem_c = stack.popleft()
        if mem_c == mem_b:
            return distance[mem_c]

        for i in liner[mem_c]:
            if distance[i] == -1:
                distance[i] = distance[mem_c] + 1
                stack.append(i)

    return -1
#========================
number = int(input())
mem_a, mem_b = map(int, input().split())
line = int(input())
liner = [[] for _ in range(number+1)]
distance = [-1] * (number+1)
distance[mem_a] = 0
for _ in range(line):
    a, b = map(int, input().split())
    liner[a].append(b)
    liner[b].append(a)

print(bfs(mem_a))