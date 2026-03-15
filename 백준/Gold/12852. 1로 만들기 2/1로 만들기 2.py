from collections import deque
n = int(input())
visited = [[-1,-1] for _ in range(n+1)]
visited[n][0] = 0
basket = deque([n])

while basket:
    X = basket.popleft()
    if X == 1:
        num_list = [1]
        while True:
            if visited[X][1] == -1:
                break
            num_list.append(visited[X][1])
            X = visited[X][1]
        break

    for order in range(3):
        if order == 0:
            if X % 3 == 0 and visited[X//3][0] == -1:
                visited[X//3][0] = visited[X][0] + 1
                visited[X//3][1] = X
                basket.append(X//3)

        elif order == 1:
            if X % 2 == 0 and visited[X//2][0] == -1:
                visited[X//2][0] = visited[X][0] + 1
                visited[X//2][1] = X
                basket.append(X//2)

        else:
            if visited[X-1][0] == -1:
                visited[X-1][0] = visited[X][0] + 1
                visited[X-1][1] = X
                basket.append(X-1)
print(visited[1][0])
print(*reversed(num_list))