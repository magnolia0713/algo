def before(std):
    pointer = std - 1
    count = 1
    if std == 0:
        return 0

    crit = height_arr[pointer] - height_arr[std]
    pointer -= 1

    while pointer >= 0:
        temp = (height_arr[pointer] - height_arr[std]) / (std - pointer)

        if temp > crit:
            crit = temp
            count += 1

        pointer -= 1

    return count

def after(std):
    pointer = std + 1
    count = 1
    if std == n-1:
        return 0

    crit = height_arr[pointer] - height_arr[std]
    pointer += 1

    while pointer < n:
        temp = (height_arr[pointer] - height_arr[std]) / (pointer - std)

        if temp > crit:
            crit = temp
            count += 1

        pointer += 1

    return count

n = int(input())
height_arr = list(map(int, input().split()))
a_max = 0

for i in range(n):
    result = before(i) + after(i)

    if a_max < result:
        a_max = result

print(a_max)
