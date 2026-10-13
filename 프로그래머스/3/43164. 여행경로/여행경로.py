
from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    # 1. 항공권 역순 정렬
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)
    
    print(graph)
    stack = ["ICN"]
    route = []

    # 2. DFS 탐색
    while stack:
        current = stack[-1]
        
        # 남은 경로가 있을 때 
        if graph[current]:
            next_airport = graph[current].pop()
            stack.append(next_airport)
        
        # 없을 때
        else:
            route.append(stack.pop())

    return route[::-1]
