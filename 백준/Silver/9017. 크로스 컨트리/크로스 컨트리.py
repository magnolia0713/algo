T = int(input())

for _ in range(T):
    n = int(input())
    num_arr = list(map(int, input().split()))
    M = [0] * 201
    check_list = set()
    for i in num_arr:
        M[i] += 1
        if M[i] >= 6:
            check_list.add(i)

    total_point = [0] * 201
    fifth = [0] * 201
    cnt = 0
    
    for i in range(n):
        if num_arr[i] in check_list:
            if fifth[num_arr[i]] <= 3:
                total_point[num_arr[i]] += cnt
                fifth[num_arr[i]] += 1

            elif fifth[num_arr[i]] == 4:
                fifth[num_arr[i]] = cnt
                
            cnt += 1

    a_min = 100000
    result = 0
    
    for i in check_list:
        if a_min > total_point[i]:
            a_min = total_point[i]
            result = i
            
        elif a_min == total_point[i]:
            if fifth[result] > fifth[i]:
                result = i

    print(result)