N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
a_sum = int(input())
head = 0
tail = N-1
count = 0
while head != tail:

    if num_list[head] + num_list[tail] == a_sum:
        count += 1
        head += 1
        if head != tail:
            tail -= 1

    else:
        if num_list[head] + num_list[tail] > a_sum:
            tail -= 1

        if num_list[head] + num_list[tail] < a_sum:
            head += 1

print(count)