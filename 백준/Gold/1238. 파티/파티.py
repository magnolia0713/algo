from heapq import heappush, heappop
import sys
input = sys.stdin.readline
# 파티 가는 길

def dijk(start):
    min_queue = [(0, start)]
    temp_memo = [100000] * (n+1)
    temp_memo[start] = 0
    while min_queue:
        value, hid = heappop(min_queue)

        if temp_memo[x] < value:
            break

        if temp_memo[hid] < value:
            continue

        for end, cost in line_dict[hid].items():
            temp_value = value + cost

            if temp_value < temp_memo[end]:
                temp_memo[end] = temp_value
                heappush(min_queue, (temp_value, end))

    return temp_memo[x]


# 오는 길

def dijk2(start):
    min_queue = [(0, start)]
    temp_memo = [100000] * (n+1)
    while min_queue:
        value, hid = heappop(min_queue)

        if temp_memo[hid] < value:
            continue

        for end, cost in line_dict[hid].items():
            temp_value = value + cost

            if temp_value < temp_memo[end]:
                temp_memo[end] = temp_value
                heappush(min_queue, (temp_value, end))

    return temp_memo

#init
n, m, x = map(int, input().split())

line_dict = [{} for _ in range(n+1)]

for _ in range(m):
    s, e, v = map(int, input().split())
    line_dict[s][e] = v

go_memo = [0] * (n + 1)
for i in range(1, n+1):
    go_memo[i] = dijk(i)

return_memo = dijk2(x)

max_value = 0
for i in range(1, n+1):
    max_value = max(max_value, go_memo[i] + return_memo[i])

print(max_value)
