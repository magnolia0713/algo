n, m = map(int, input().split())

coord = [-1]
for _ in range(n):
    x, y = map(int, input().split())
    coord.append(y)

roads = []
for _ in range(m):
    s, e, value = map(int, input().split())
    start = coord[s]
    end = coord[e]

    if start > end:
        start, end = end, start

    roads.append((start,value))
    roads.append((end+1, -value))

roads.sort()

a_max = 0
a_present = 0

for _, value in roads:
    a_present += value
    if a_max < a_present:
        a_max = a_present

print(a_max)
