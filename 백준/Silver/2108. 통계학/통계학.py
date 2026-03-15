import sys
N = int(input())
list_num = [0] * 8001

#0. 리스트에 숫자 입력
for _ in range(N):
    a = int(sys.stdin.readline())
    list_num[a+4000] += 1

#1. 평균
sum_a = 0
for i in range(8001):
    sum_a += list_num[i] * (i - 4000)

avg_a = sum_a / sum(list_num)
if avg_a % 1 >= 0.5:
    avg_a += 1

print(int(avg_a // 1))

#2. 중앙값
finding_num = (N+1) / 2
counter = 0
for i in range(8001):
    counter += list_num[i]
    if counter >= finding_num:
        print(i-4000)
        break


#3. 최빈값
max_a = max(list_num)
max_count = 0
if list_num.count(max_a) >= 2:
    for i in range(8001):
        if max_a == list_num[i]:
            max_count += 1
            if max_count == 2:
                print(i-4000)
                break
else:
    print(list_num.index(max_a) - 4000)
#4. 범위
for i in range(8001):
    if list_num[i] != 0:
        min_num = i
        break

for j in range(8000, -1 ,-1):
    if list_num[j] != 0:
        max_num = j
        break

print(max_num - min_num)