def king(node):
    if my_lord[node] != node:
        my_lord[node] = king(my_lord[node])

    return my_lord[node]

def union(node1, node2):
    
    my_lord[king(node2)] = my_lord[king(node1)]
    return
    

n = int(input())
my_lord = list(range(0, n+1))
enemy = [0] * (n+1)
lines = int(input())

for _ in range(lines):
    status, start, end = input().split()
    start = int(start); end = int(end)
    if status == 'F':
        if king(start) != king(end):
            union(start, end)
    
    else:
        if enemy[start]:
            if king(enemy[start]) != king(end):
                union(enemy[start], end)

        else:
            enemy[start] = end

        if enemy[end]:
            if king(enemy[end]) != king(start):
                union(enemy[end], start)
        else:
            enemy[end] = start

for i in range(1, n+1):
    king(i)

ans = len(set(my_lord))
print(ans - 1)
