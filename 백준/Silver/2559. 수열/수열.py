n, k = map(int, input().split())
n_list = list(map(int, input().split()))
init = sum(n_list[0:k])
a_max = init

for i in range(1, n-k+1):
    init += (n_list[i+k-1] - n_list[i-1])

    if a_max < init:
        a_max = init
print(a_max)
    