from collections import deque
n = int(input())
order_list = []
n_list = deque((range(1, n+1)))

i = 1
while n_list:
    temp = n_list.popleft()
    if i:
        order_list.append(temp)
        i = 0

    else:
        n_list.append(temp)
        i = 1

print(*order_list)