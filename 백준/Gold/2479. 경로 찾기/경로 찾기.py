from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

node_list = []

for i in range(n):
    node_list.append(input().strip())

node_sum = [[] for _ in range(k+1)]
for i in range(len(node_list)):
    cnt = 0
    for j in node_list[i]:
        if int(j):
            cnt += 1
    node_sum[cnt].append((node_list[i],i))


#그래프 형성
graph = [[] for _ in range(n+1)]

for i in range(k+1):

    if i >= 1:
        for num1, idx1 in node_sum[i-1]:
            for j in range(len(node_sum[i])):
                num2, idx2 = node_sum[i][j]
                count = 0
                for digit in range(k):
                    if num1[digit] != num2[digit]:
                        count += 1
                        if count > 1:
                            break

                else:
                    graph[idx1].append(idx2)
                    graph[idx2].append(idx1)


trace = [[i] for i in range(n)]
visited = [0] * n

# 이제 bfs 시작
s, e = map(int, input().split())
s -= 1
e -= 1
basket = deque()
basket.append(s)

def bfs():
    while basket:
        node = basket.popleft()

        for i in graph[node]:
            if not visited[i]:
                trace[i] = trace[node] + [i]
                visited[i] = 1
                basket.append(i)
                if i == e:
                    return

bfs()
if len(trace[e]) == 1:
    print(-1)
else:
    for i in trace[e]:
        print(i+1,end=' ')

