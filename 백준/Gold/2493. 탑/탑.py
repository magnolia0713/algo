n = int(input())
n_list = list(map(int, input().split())) 

stack = [] 
ans = [0] * n

for i in range(n):
    current_height = n_list[i]
    
    while stack and stack[-1][1] < current_height:
        stack.pop()
    
    if stack:
        ans[i] = stack[-1][0] + 1 
    
    stack.append((i, current_height))

print(*ans)
