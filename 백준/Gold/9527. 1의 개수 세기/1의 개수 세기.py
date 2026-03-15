

start, end = map(int, input().split())
p = end
cnt = 0
while p:
    cnt += 1
    p //= 2
total_cnt = 0

for i in range(1, cnt+1):
    temp = 2 ** i
    start_value, start_remains = divmod(start, temp)
    end_value, end_remains = divmod(end, temp)
    #가운데 있는 값들은 바로 더하고
    total_cnt += (end_value - start_value - 1) * temp // 2

    #처음 값
    temp_start = temp - start_remains

    if temp_start > temp//2:
        temp_start = temp//2
    total_cnt += temp_start

    #마지막 값
    temp_end = (end_remains + 1) - (temp//2)
    if temp_end < 0:
        temp_end = 0
    total_cnt += temp_end

print(total_cnt)