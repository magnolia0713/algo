N = int(input())
 
graph = [[0] * (N+1) for _ in range(N+1)]
 
for i in range(1, N):
  temp = int(input())
  a = list(map(int, input().split()))
 
  for j in a:
    graph[i][j] = 1
 
 
 
 
for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      if graph[i][k] and graph[k][j]:
        graph[i][j] = 1
 
 
ans = "NO CYCLE"
 
for i in range(1, N+1):
  if graph[1][i] == 1 and graph[i][i] == 1:
    ans = "CYCLE"
 
print(ans)