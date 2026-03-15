def iamqueen(level):
    global count

    if level == N:
        count += 1

    for c in range(N):
        if c in queen_c:
            for n, m in visited:
                if level + c == n + m:
                    break
                if level - n == c - m:
                    break

            else:
                queen_c.remove(c)
                visited.add((level,c))
                iamqueen(level+1)
                visited.remove((level,c))
                queen_c.add(c)

N = int(input())
visited = set()
queen_c = set(range(N))
count = 0
iamqueen(0)

print(count)