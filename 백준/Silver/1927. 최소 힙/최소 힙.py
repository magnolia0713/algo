import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
n_list = []

for _ in range(n):
    n_list.append(int(input()))

hq = []

for i in n_list:
    if i != 0:
        heappush(hq, i)

    else:
        if hq:
            print(heappop(hq))
        else:
            print(0)
