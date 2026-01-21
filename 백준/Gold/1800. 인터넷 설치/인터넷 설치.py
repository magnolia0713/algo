import sys
from collections import deque

input = sys.stdin.readline
INF = 10**9

def feasible(X, n, graph, K):
    # dist[v] = 1 -> v 가는 동안 "비싼 간선(비용>X)"을 쓴 최소 개수
    dist = [INF] * (n + 1)
    dist[1] = 0
    dq = deque([1])

    while dq:
        u = dq.popleft()
        du = dist[u]
        if du > K:  # 이미 K 초과면 더 볼 가치 적음(가지치기)
            continue
        for v, w in graph[u]:
            cost = 0 if w <= X else 1
            nd = du + cost
            if nd < dist[v]:
                dist[v] = nd
                if cost == 0:
                    dq.appendleft(v)  # 0 간선은 앞에
                else:
                    dq.append(v)      # 1 간선은 뒤에

    return dist[n] <= K

def solve():
    n, p, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    max_w = 0

    for _ in range(p):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        if c > max_w:
            max_w = c

    # 연결 자체가 불가능하면 -1 (X=max_w로도 못 가면)
    if not feasible(max_w, n, graph, k):
        print(-1)
        return

    lo, hi = 0, max_w
    ans = max_w
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid, n, graph, k):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)

if __name__ == "__main__":
    solve()