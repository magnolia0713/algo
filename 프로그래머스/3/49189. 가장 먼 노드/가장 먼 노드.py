from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
        
    answer = bfs(n, graph)
    
    return answer
    # bfs를 활용하자.
    

def bfs(n, graph):
    
    basket = deque()
    basket.append(1)
    visited = [0] * (n+1)
    visited[1] = 1
    cnt = 0
    while basket:
        
        prev_cnt = cnt
        cnt = 0
        
        for _ in range(len(basket)):
            curr_node = basket.popleft()

            for nxt_node in graph[curr_node]:

                # 이미 방문한 노드 처리
                if visited[nxt_node]:
                    continue

                # 그 외
                visited[nxt_node] = 1
                cnt += 1
                basket.append(nxt_node)
        
    return prev_cnt
    
    return answer

