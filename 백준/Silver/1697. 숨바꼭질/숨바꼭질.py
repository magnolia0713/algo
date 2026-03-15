from collections import deque

def bfs(start, end):
    if start == end:
        return 0


    distance[start] = 0
    basket = deque([start])
    while basket:
        r = basket.popleft()
        for i in range(3):
            if i == 0:
                nr = r + 1
            elif i == 1:
                nr = r - 1
            else:
                nr = r * 2
            if 0 <= nr < 150000 and distance[nr] == -1:
                basket.append(nr)
                distance[nr] = distance[r] + 1

                if nr == end:
                    return distance[nr]

#----------------------------------------------------------------------

start, end = map(int, input().split())
distance = [-1] * 150001
result = bfs(start, end)
print(result)
