import sys
input = sys.stdin.readline
from collections import deque

def sorting():

    while basket:
        p = basket.popleft()
        if end_graph[p]:
            times[p] = max(times[k] for k in end_graph[p]) + time_list[p-1]

        else:
            times[p] = time_list[p-1]

        if times[to_win] >= 0:
            return times[to_win]

        for j in graph[p]:
            visited[j] -= 1
            if not visited[j]:
                basket.append(j)


t = int(input())

for _ in range(t):
    node, lines = map(int, input().split())
    time_list = list(map(int, input().split()))

    graph = [[] for _ in range(node+1)]
    end_graph = [[] for _ in range(node+1)]
    visited = [0] * (node+1)
    times = [-1] * (node+1)
    for _ in range(lines):
        start, end = map(int, input().split())
        graph[start].append(end)
        end_graph[end].append(start)
        visited[end] += 1

    to_win = int(input())

    basket = deque()
    for i in range(1, node+1):
        if not visited[i]:
            basket.append(i)

    print(sorting())