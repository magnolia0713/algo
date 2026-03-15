n = int(input())
n_list = list(map(int, input().split()))
a_max = int(input())
n_list.sort()
mini_sum = 0
for i in range(n):
    mini_sum += n_list[i]
    if n_list[i] * (n-i-1) + mini_sum > a_max:
        p = ((n_list[i] * (n-i-1) + mini_sum) - a_max) // (n-i)
        if ((n_list[i] * (n-i-1) + mini_sum) - a_max) % (n-i) != 0:
            res = n_list[i] - (p + 1) 

        else:
            res = n_list[i] - p
        print(res)
        break
else:
    print(n_list[n-1])
    