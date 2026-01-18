import heapq
from heapq import heappush, heappop

n = int(input())
at_first = int(input())
ans_list = [at_first]
left_heap = []
right_heap = []
heappush(left_heap, -at_first)

for i in range(n-1):
    num = int(input())
    if len(left_heap) > len(right_heap):
        temp = -heappop(left_heap)
        a, b = min(num, temp), max(num, temp)

        heappush(left_heap, -a)
        heappush(right_heap, b)
        ans_list.append(-left_heap[0])

    else:
        temp = heappop(right_heap)
        a, b = min(num, temp), max(num, temp)

        heappush(left_heap, -a)
        heappush(right_heap, b)
        ans_list.append(-left_heap[0])


print('\n'.join(map(str, ans_list)))
