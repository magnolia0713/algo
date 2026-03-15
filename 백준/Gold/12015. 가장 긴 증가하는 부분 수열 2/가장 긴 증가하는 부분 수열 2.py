
n = int(input())
n_list = list(map(int, input().split()))

def indexing(start, end, num):

    while start <= end:
        mid = (start + end) // 2

        if a_list[mid] < num:
            start = mid + 1

        else:
            end = mid - 1

    return start if start < len(a_list) else -1

a_list = [n_list[0]]

for i in range(1, len(n_list)):
    idx = indexing(0, len(a_list) - 1, n_list[i])

    if idx == -1:
        a_list.append(n_list[i])
    else:
        a_list[idx] = n_list[i]
print(len(a_list))
