# 트리와 쿼리 2
# 문제 핵심 : binary lifting(트리의 이진탐색 버전, 일종의 dp)
n = int(input())

max_length = n.bit_length()
lifting_dp = [[0] * (n+1) for _ in range(max_length)]
dist_dp = [0] * (n+1)
weight_dp = [0] * (n+1)

tree_graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, w = map(int, input().split())
    tree_graph[s].append((e, w))
    tree_graph[e].append((s, w))

# dist_dp / weight_dp / lifting_dp[0] (부모) 를 같이 채우기
root = 1
visited = [0] * (n+1)
visited[root] = 1
dist_dp[root] = 0
weight_dp[root] = 0
lifting_dp[0][root] = 0  # 루트의 부모는 0

basket = [root]
while basket:
    node = basket.pop()
    for nxt_node, w in tree_graph[node]:
        if not visited[nxt_node]:
            visited[nxt_node] = 1

            lifting_dp[0][nxt_node] = node
            dist_dp[nxt_node] = dist_dp[node] + 1
            weight_dp[nxt_node] = weight_dp[node] + w

            basket.append(nxt_node)

for k in range(1, max_length):
    for node in range(1, n+1):
        lifting_dp[k][node] = lifting_dp[k-1][lifting_dp[k-1][node]]
# print(tree_graph)
# print(lifting_dp)
# print(dist_dp)
# print(weight_dp)
# --------------------- 전처리 완료. 이제 계산을 해보자.

queries = int(input())

for _ in range(queries):
    query = list(map(int, input().split()))

    # 가는데 드는 비용 계산
    if query[0] == 1:
        s, e = query[1], query[2]
        org_s = s
        org_e = e

        # 일단 depth를 맞춰두자.
        if dist_dp[s] > dist_dp[e]:
            diff = dist_dp[s] - dist_dp[e]
            cnt = 0
            while diff:
                diff, needed = divmod(diff, 2)
                if needed:
                    s = lifting_dp[cnt][s]
                cnt += 1

        if dist_dp[s] < dist_dp[e]:
            diff = dist_dp[e] - dist_dp[s]
            cnt = 0
            while diff:
                diff, needed = divmod(diff, 2)
                if needed:
                    e = lifting_dp[cnt][e]
                cnt += 1
        # 이제 노드의 depth를 맞췄으니, 서로 공통조상을 찾아주자.
        height = max_length - 1
        if s == e:
            ans = (weight_dp[org_s] + weight_dp[org_e] - 2 * weight_dp[s])

        else:
            while height >= 0:
                if lifting_dp[height][s]:
                    if lifting_dp[height][s] == lifting_dp[height][e]:
                        temp = lifting_dp[height][s]
                        height -= 1
                        #어디가 마지막 공통 조상인지 파악, 근데 약간 미숙한 것 같은데?
                    else:
                        s = lifting_dp[height][s]
                        e = lifting_dp[height][e]
                else:
                    height -= 1
            ans = (weight_dp[org_s] + weight_dp[org_e] - 2 * weight_dp[temp])

    else:
        s, e, d = query[1], query[2], query[3] - 1
        org_s = s
        org_e = e
        # 일단 depth를 맞춰두자.
        if dist_dp[s] > dist_dp[e]:
            diff = dist_dp[s] - dist_dp[e]
            cnt = 0
            while diff:
                diff, needed = divmod(diff, 2)
                if needed:
                    s = lifting_dp[cnt][s]
                cnt += 1

        if dist_dp[s] < dist_dp[e]:
            diff = dist_dp[e] - dist_dp[s]
            cnt = 0
            while diff:
                diff, needed = divmod(diff, 2)
                if needed:
                    e = lifting_dp[cnt][e]
                cnt += 1
        # 이제 노드의 depth를 맞췄으니, 서로 공통조상을 찾아주자.
        height = max_length - 1
        if s == e:
            temp = s
        else:
            while height >= 0:
                if lifting_dp[height][s]:
                    if lifting_dp[height][s] == lifting_dp[height][e]:
                        temp = lifting_dp[height][s]
                        height -= 1
                        #어디가 마지막 공통 조상인지 파악, 근데 약간 미숙한 것 같은데?
                    else:
                        s = lifting_dp[height][s]
                        e = lifting_dp[height][e]
                        height -= 1
                else:
                    height -= 1

        # 인덱스 검색
        diff = dist_dp[org_s] - dist_dp[temp]
        s = org_s; e = org_e
        if diff > d:
            cnt = 0
            while d:
                d, needed = divmod(d, 2)
                if needed:
                    s = lifting_dp[cnt][s]
                cnt += 1
            ans = s
        elif diff == d:
            ans = temp

        else:
            d -= diff
            d = (dist_dp[org_e] - dist_dp[temp]) - d
            if not d:
                ans = org_e

            else:
                cnt = 0
                while d:
                    d, needed = divmod(d, 2)
                    if needed:
                        e = lifting_dp[cnt][e]
                    cnt += 1
                ans = e


    print(ans)