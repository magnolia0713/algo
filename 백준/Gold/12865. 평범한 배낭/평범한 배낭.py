def DP(depth, weight):

    if K < weight:
        return -999999

    if depth == N:
        return 0

    if (depth, weight) in memo_dict:
        return memo_dict[(depth, weight)]
    else:
        result = max(DP(depth + 1, weight), a_list[depth][1] + DP(depth + 1, weight + a_list[depth][0]))
        memo_dict[(depth, weight)] = result
        return memo_dict[(depth, weight)]

N, K = map(int, input().split())
a_list = []
memo_dict = {}

for _ in range(N):
    i, j = map(int, input().split())
    a_list.append((i,j))

max_a = 0
print(DP(0,0))