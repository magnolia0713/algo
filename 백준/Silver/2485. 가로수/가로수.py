n = int(input())

n_list = []

for _ in range(n):
    n_list.append(int(input()))

n_length = n_list[1] - n_list[0]

for i in range(2, n):
    temp = n_list[i] - n_list[i-1]
    if temp == n_length:
        continue

    a, b = max(temp, n_length), min(temp, n_length)

    while True:
        p = a % b
        if not p:
            n_length = b
            break

        a, b = max(b, p), min(b, p)
print((n_list[-1] - n_list[0]) // n_length - n + 1)