n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

head = 0
tail = len(num_list) - 1

a_min = abs(num_list[head] + num_list[tail])
a_value = num_list[head]
b_value = num_list[tail]

while head != tail:
    if a_min > abs(num_list[head] + num_list[tail]):
        a_min = abs(num_list[head] + num_list[tail])
        a_value = num_list[head]
        b_value = num_list[tail]

    if num_list[head] + num_list[tail] > 0:
        tail -= 1

    elif num_list[head] + num_list[tail] < 0:
        head += 1


    else:
        a_value = num_list[head]
        b_value = num_list[tail]
        break

print(a_value, b_value)