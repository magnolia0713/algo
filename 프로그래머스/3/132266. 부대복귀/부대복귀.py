def solution(n, roads, sources, destination):
    
    from collections import deque
    
    answer = []
    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    # 그래프 생성
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    # bfs로 접근.
    basket = deque()
    basket.append(destination)
    visited[destination] = 0
    
    while basket:
        t = basket.popleft()
        for i in graph[t]:
            if visited[i] == -1:
                basket.append(i)
                visited[i] = visited[t] + 1
                
    for i in sources:
        answer.append(visited[i])
        
    
    return answer