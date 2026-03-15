n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort(reverse=True)
n_list.append(0)

for i in range(n):
    length = n_list[i] - n_list[i+1]
    if m > length * (i+1):
        m -= length * (i+1)

    else:
        size = (m-1) // (i+1) + 1
        break

print(n_list[i] - size)

