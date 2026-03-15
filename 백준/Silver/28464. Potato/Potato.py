n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

half = n // 2
print(sum(n_list[:half]), sum(n_list[half:]))