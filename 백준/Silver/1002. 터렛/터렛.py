

t = int(input())

for _ in range(t):
    a,b,x,c,d,y = map(int, input().split())
    if a == c and b == d and x == y:
        print(-1)
    else:
        #print(a, b, x, c, d, y)
        dist = ((a-c) ** 2) + ((b-d) ** 2)
        #print(dist)

        if dist < (x-y) ** 2:
            print(0)

        elif dist == (x-y) ** 2:
            print(1)

        elif dist < (x+y) ** 2:
            print(2)

        elif dist == (x+y) ** 2:
            print(1)

        else:
            print(0)