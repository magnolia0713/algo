import sys
from heapq import heappush, heappop

input = sys.stdin.readline

test_case = int(input())
inf = 1e12
for _ in range(test_case):
    n, p, q = map(int, input().split())
    # 출발노드,
    matrix = [[inf] * (p+1) for _ in range(n)]

    # 탐색 대상노드 지정
    node_list = []
    for i in range(n):
        node_list.append(int(input()))

    # 그래프 형성
    graph = [[] for _ in range(p+1)]
    for _ in range(q):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        graph[e].append((s, w))

    # 다익스트라
    def dijk(idx, init):
        pq = []
        heappush(pq, (0, init))

        while pq:
            weight, node = heappop(pq)

            # 쓸데 없는 정보 cut
            if matrix[idx][node] < weight:
                continue

            matrix[idx][node] = weight

            for nxt_node, nxt_weight in graph[node]:
                t_weight = weight + nxt_weight
                if matrix[idx][nxt_node] > t_weight:
                    matrix[idx][nxt_node] = t_weight
                    heappush(pq, (t_weight, nxt_node))

        return

    for i in range(len(node_list)):
        dijk(i, node_list[i])

    # ans_sheet 에 토탈을 적자.
    ans_sheet = [inf] * (p+1)
    for i in range(1, p+1):
        a_sum = 0
        for j in range(n):
            a_sum += matrix[j][i] ** 2

        ans_sheet[i] = a_sum

    min_ans = inf
    min_node = 0
    for node in range(1, p+1):
            if min_ans > ans_sheet[node]:
                min_ans = ans_sheet[node]
                min_node = node

    print(min_node, min_ans)
