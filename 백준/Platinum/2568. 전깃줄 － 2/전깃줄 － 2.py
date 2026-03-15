
n = int(input())
n_list = []

def bi_sect(start, end, num):

    while start <= end:
        mid = (start + end) // 2
        if num < memo[mid]:
            end = mid - 1

        elif num > memo[mid]:
            start = mid + 1

        else:
            start = mid
            break

    return start

for _ in range(n):
    n_list.append(tuple(map(int, input().split())))
n_list.sort()
inf = 1e6
memo = [inf] * (n+1)
numbers = [[] for _ in range(n)]
pointer = 0
for start, end in n_list:
    idx = bi_sect(0, pointer+1, end)
    memo[idx] = end

    if idx == pointer:
        pointer += 1
    numbers[idx].append(start)

init = 1e6
ans_box = []

for i in range(pointer-1, -1, -1):
    for value in range(len(numbers[i])-1, -1, -1):
        if init > numbers[i][value]:
            init = numbers[i][value]
            ans_box.extend(numbers[i][0:value])
            ans_box.extend(numbers[i][value+1:])
            break
ans_box.sort()
print(len(ans_box))
print(*ans_box, sep='\n')