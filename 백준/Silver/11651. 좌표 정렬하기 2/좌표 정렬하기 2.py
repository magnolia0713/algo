T = int(input())

list_a = []

for _ in range(T):
    a, b = map(int, input().split())
    list_a.append((a, b))

list_a.sort(key = lambda x : (x[1],x[0]))

for tuple_a in list_a:
    print(*tuple_a)