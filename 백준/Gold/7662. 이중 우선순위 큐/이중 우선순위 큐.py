
import heapq, sys

input = sys.stdin.readline

heappush = heapq.heappush
heappop = heapq.heappop

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    id_storage = [False] * k
    for i in range(k):
        key, value = input().split()
        if key == 'I':
            value = int(value)
            heappush(min_heap, (value, i))
            heappush(max_heap, (-value, i))
            id_storage[i] = True



        else:
            if value == '1':

                while max_heap:
                    value, vid = heappop(max_heap)

                    if id_storage[vid]:
                        id_storage[vid] = False
                        break

            else:
                while min_heap:
                    value, vid = heappop(min_heap)

                    if id_storage[vid]:
                        id_storage[vid] = False
                        break

    ans = []
    while max_heap:
        value, vid = heappop(max_heap)

        if id_storage[vid]:
            ans.append(-value)
            break

    if not ans:
        print('EMPTY')

    else:
        while min_heap:
            value, vid = heappop(min_heap)

            if id_storage[vid]:
                ans.append(value)
                break

        print(*ans)