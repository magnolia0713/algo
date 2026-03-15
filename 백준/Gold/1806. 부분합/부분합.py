


n, s = map(int, input().split())

num_arr = list(map(int, input().split()))
head = 0
tail = 0
a_sum = num_arr[0]
a_min = 111111

while tail < n:

    if a_sum < s:
        if tail == n-1:
            break
        tail += 1
        a_sum += num_arr[tail]

    elif a_sum >= s:
        a_min = min(a_min, tail - head + 1)
        if head == tail:
            break

        a_sum -= num_arr[head]
        head += 1


if a_sum == s:
    a_min = min(a_min, tail - head + 1)

if a_min == 111111:
    a_min = 0

print(a_min)

