n = int(input())
m = list(input())
cnt = 0
for i in range(len(m) -1, -1, -1):
    temp = n * int(m[i])
    cnt += (10 ** (len(m) - i-1)) * temp
    print(temp)

print(cnt)
    
