a, d = map(int, input().split())
b, e = map(int, input().split())
c, f = map(int, input().split())

if a == c:
    x = b
elif b == c:
    x = a
else:
    x = c

if d == e:
    y = f
elif e == f:
    y = d
else:
    y = e

print(x,y)