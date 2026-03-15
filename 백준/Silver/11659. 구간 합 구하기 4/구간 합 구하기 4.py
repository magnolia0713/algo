N, M = map(int, input().split())
a_list = list(map(int, input().split()))
a_prefix = [0] * (N+1)
a_prefix[1] = a_list[0]
for i in range(2,N+1):
    a_prefix[i] += a_prefix[i-1] + a_list[i-1]
for _ in range(M):
    a, b = map(int, input().split())
    print(a_prefix[b]-a_prefix[a-1])