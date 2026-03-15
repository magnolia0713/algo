T = int(input())

score_list = []

for t in range(T):
    a = int(input())
    score_list.append(a)

try_number = 0


for i in range(1,T):
    if score_list[i] <= score_list[i-1]:
        for j in range(i):
            if score_list[j] >= score_list[i]-(i-j):
                try_number += (score_list[j] - score_list[i] + (i - j))
                score_list[j] = score_list[i] - (i - j)


print(try_number)