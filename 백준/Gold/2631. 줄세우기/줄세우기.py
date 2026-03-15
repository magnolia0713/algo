import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
num_arr = []

for _ in range(n):
    num_arr.append(int(input()))

memo = [defaultdict(lambda:200) for _ in range(n)]

memo[0][1] = num_arr[0]

for i in range(1, n):
    temp_val = num_arr[i]
    if memo[i][1] > temp_val:
        memo[i][1] = temp_val  
      
    for cnt, value in memo[i-1].items():
        if value < temp_val and memo[i][cnt+1] > temp_val:
            memo[i][cnt+1] = temp_val

        if memo[i][cnt] > value:
            memo[i][cnt] = value

print(n - max(memo[n-1]))