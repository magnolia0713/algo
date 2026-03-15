n = int(input())
n_list = list(map(int, input().split()))

def indexing(start, end, num):

    while start <= end:
        mid = (start + end) // 2

        if a_list[mid][-1][0] < num:
            start = mid + 1

        else:
            end = mid - 1

    return start
inf = 1e9
a_list = [[(inf, -1)] for _ in range(n)]
a_list[0].append((n_list[0], 0))

pointer = 0
for i in range(1, len(n_list)):

    idx = indexing(0, len(a_list) - 1, n_list[i])
    a_list[idx].append((n_list[i], i))
final_idx = n
final_value = inf
b_list = []
for i in range(n-1, -1, -1):
    for value, idx in a_list[i]:
        if value == inf:
            continue

        if final_value > value and final_idx > idx:
            final_value = value; final_idx = idx
            b_list.append(value)
            break
print(len(b_list))
print(*reversed(b_list))