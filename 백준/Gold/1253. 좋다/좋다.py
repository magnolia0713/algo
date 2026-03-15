from collections import Counter

n = int(input())
num_list = list(map(int, input().split()))

counter = sorted(list(Counter(num_list).items()))
lengths = len(counter)
check = [False] * lengths
zeros = -1
tc = 0

for i in range(lengths):
    pointer = 0
    if counter[i][0] == 0:
        zeros = i
        for index in range(lengths):
            if counter[index][1] > 1 and counter[index][0] != 0:
                check[index] = True
        continue

    if counter[i][1] < 2:
        p = i + 1
    else:
        p = i

    for j in range(p, lengths):

        while pointer < lengths:
            temp = counter[i][0] + counter[j][0]

            if temp == counter[pointer][0] and pointer not in [i,j]:
                check[pointer] = True

            elif temp < counter[pointer][0]:
                break

            pointer += 1


if zeros != -1 and counter[zeros][1] > 2:
    check[zeros] = True


for i in range(lengths):
    if check[i]:
        tc += counter[i][1]

print(tc)


