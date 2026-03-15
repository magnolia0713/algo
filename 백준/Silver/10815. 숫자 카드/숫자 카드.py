a = int(input())
set_a = set(map(int, input().split()))

b = int(input())
list_b = list(map(int, input().split()))

for t in range(len(list_b)):

    if list_b[t] in set_a:
        list_b[t] = 1

    else:
        list_b[t] = 0

print(*list_b)