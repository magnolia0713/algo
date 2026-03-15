N = int(input())
num_list = list(map(int, input().split()))

memo = [1]*N

for i in range(N):
    for j in range(i):
        if num_list[j] < num_list[i]:
            memo[i] = max(memo[i], memo[j]+1)
            
print(max(memo))