def solution(n, computers):
    answer = 0
    visited = [0] * n
    basket = []
    
    for i in range(n):
        
        if not visited[i]:
            answer += 1
            visited[i] = 1
            basket.append(i)
            
            while basket:
                node = basket.pop()
                
                for j in range(n):
                    if computers[node][j] and not visited[j]:
                        basket.append(j)
                        visited[j] = 1
                        
                
            
        print(visited)
    
    return answer