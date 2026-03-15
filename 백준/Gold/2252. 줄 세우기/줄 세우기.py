from collections import deque
import sys

input = sys.stdin.readline

def sorting():
    basket = deque()
    for i in range(1, n+1):
        if not num_of_line[i]:
            basket.append(i)

    while basket:
        p = basket.popleft()
        sorted_list.append(p)

        for j in graph[p]:
            num_of_line[j] -= 1
            if not num_of_line[j]:
                basket.append(j)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
num_of_line = [0] * (n+1)
sorted_list = []

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    num_of_line[end] += 1

sorting()
print(*sorted_list)
