N, M = map(int, input().split())

score_list = list(map(int, input().split()))

stu_list = []
for number in range(M):

    list_a = list(input().split())
    stu_list.append(list_a)
for i in range(M):
    stu_list[i][0] =  int(stu_list[i][0])
    
stu_list.sort(key = lambda x:x[0])

for i in range(M):
    for j in range(1,N+1):
        if stu_list[i][j] == 'O':
            stu_list[i][j] = 1
        else:
            stu_list[i][j] = 0
        
max_score = 0
max_stu = stu_list[0][0]

for number in range(M):
    sub_total = 0
    for i in range(len(score_list)):
        sub_total += stu_list[number][i+1] * score_list[i]
    if sub_total > max_score:
        max_score = sub_total
        max_stu = stu_list[number][0]

print(int(max_stu), max_score)