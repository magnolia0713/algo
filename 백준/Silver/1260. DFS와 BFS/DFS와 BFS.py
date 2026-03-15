from collections import deque
def bfs(start):
    stack = deque([start])
    while stack:
        num_bfs = stack.popleft()
        for i in range(node):
            if matrix[num_bfs][i] == 1 and i not in visited:
                stack.append(i)
                visited.append(i)

def dfs(start):
    for i in range(node):
        if matrix[start][i] == 1 and i not in visited:
            visited.append(i)
            dfs(i)

node, line, start = map(int, input().split())
node += 1
matrix = [[0] * node for _ in range(node)]

for _ in range(line):
    num1, num2 = map(int,input().split())
    matrix[num1][num2] = matrix[num2][num1] = 1

visited = [start]
dfs(start)
print(*visited)

visited = [start]
bfs(start)
print(*visited)