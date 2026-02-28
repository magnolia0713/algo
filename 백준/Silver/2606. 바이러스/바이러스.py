def bfs(start):
    contaminated_set.add(start)
    basket = [start]
    while basket:
        r = basket.pop()

        for i in line_matrix[r]:
            if i not in contaminated_set:
                basket.append(i)
                contaminated_set.add(i)

    return len(contaminated_set)

N = int(input())
lines = int(input())
line_matrix = [[] for _ in range(N+1)]
contaminated_set = set()
for _ in range(lines):
    a, b = map(int, input().split())
    line_matrix[a].append(b)
    line_matrix[b].append(a)
result = bfs(1)
print(result-1)