n, m = map(int, input().split())

road = list(range(m+1))

way = []

for _ in range(n):
    way.append(list(map(int, input().split())))

way.sort()

for start, end, point in way:
    for i in range(end, m+1):
        road[i] = min(road[i], road[start] + point + (i - end))

print(road[-1])
