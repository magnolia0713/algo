n = int(input())

n_list = list(map(int, input().split()))

n_list.sort(reverse=True)

print(sum(n_list[0:(n+1)//2]) - sum(n_list[(n+2)//2:]))
