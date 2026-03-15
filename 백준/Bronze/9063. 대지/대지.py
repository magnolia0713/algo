T = int(input())

list_x = []
list_y = []
for _ in range(T):
    a, b = map(int, input().split())
    list_x.append(a)
    list_y.append(b)

X = max(list_x) - min(list_x) 
Y = max(list_y) - min(list_y)

print(X * Y)