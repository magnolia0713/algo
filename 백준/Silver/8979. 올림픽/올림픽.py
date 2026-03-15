N, K = map(int,input().split())

matrix = list(list(map(int, input().split())) for _ in range(N))

rank = 1
location = -1
for i in range(N):
    if matrix[i][0] == K:
        location = i
        break
        
for i in range(N):
    if matrix[i][1] > matrix[location][1]:
        rank += 1
    elif matrix[i][1] == matrix[location][1]:

        if matrix[i][2] > matrix[location][2]:
            rank += 1

        elif matrix[i][2] == matrix[location][2]:
            
            if matrix[i][3] > matrix[location][3]:
                rank += 1

print(rank)