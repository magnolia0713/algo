def solution(n, works):
    answer = 0
    top = max(works)
    arr = [0] * 50001
    
    for i in works:
        arr[i] += 1
        
    print(sum(arr))
    
    while n and arr[0] != len(works):
        
        if n >= arr[top]:
            arr[top-1] += arr[top]
            n -= arr[top]
            arr[top] = 0
            top -= 1
            
        else:
            arr[top-1] += n
            arr[top] -= n
            n = 0
    
    for i in range(top+1):
        answer += (i**2) * arr[i]
    
    return answer