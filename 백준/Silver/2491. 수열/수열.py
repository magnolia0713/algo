
n = int(input())
n_list = list(map(int, input().split()))

a_cnt = b_cnt = 1
max_cnt = 0
temp_a = temp_b = n_list[0]

if n == 1:
    print(1)

else:
    for i in range(n-1):
        if n_list[i+1] >= n_list[i]:
            a_cnt += 1

        else:
            if max_cnt < a_cnt:
                max_cnt = a_cnt
            a_cnt = 1

        if n_list[i+1] <= n_list[i]:
            b_cnt += 1

        else:
            if max_cnt < b_cnt:
                max_cnt = b_cnt
            b_cnt = 1

        #print(a_cnt, b_cnt)
    else:
        max_cnt = max(max_cnt, a_cnt, b_cnt)

    print(max_cnt)

