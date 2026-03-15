n = int(input())

num_list = list(map(int, input().split()))
order = [0] * n
for i in range(1, n+1):
    count = 0
    for j in range(n):
        if order[j] == 0:
            if count == num_list[i-1]:
                order[j] = i
                break
            else:
                count += 1

print(*order)