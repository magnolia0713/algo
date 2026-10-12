from heapq import heappush, heappop


def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    for node, nxt_node, weight in costs:
        graph[node].append((nxt_node, weight))
        graph[nxt_node].append((node, weight))
    
    print(graph)
    # mst
    visited = set()
    heap = [(0, 0)] #[가중치, 정점]
    
    while heap:
        w, node = heappop(heap)
        
        if node in visited:
            continue
        
        
        visited.add(node)
        answer += w
            
        for nxt_node, weight in graph[node]:
            heappush(heap, (weight, nxt_node))
            
        
    
    
    return answer