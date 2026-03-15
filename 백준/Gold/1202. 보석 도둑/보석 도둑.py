
import sys
input = sys.stdin.readline

from heapq import heappop,heappush
n, k = map(int, input().split())
treasure_list = []

for _ in range(n):
    treasure_list.append(tuple(map(int, input().split())))
treasure_list.sort()

bag_list = []
for _ in range(k):
    bag_list.append(int(input()))
bag_list.sort()

total_value = 0
queue = []
pointer = 0

for i in bag_list:
    #힙에 추가
    while pointer < n:
        if i < treasure_list[pointer][0]:
            break
        heappush(queue, -treasure_list[pointer][1])
        pointer += 1

    #힙에서 빼기
    if queue:
        total_value -= heappop(queue)

print(total_value)