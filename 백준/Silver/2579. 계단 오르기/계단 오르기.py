def DP(level,goal):
    if goal < 3:
        return max_score[level][goal]

    else:
        if level == 1:
            if max_score[level][goal] == 0:
                max_score[1][goal] = max(DP(1, goal-2), DP(2, goal-2)) + max_score[0][goal]
                return max_score[1][goal]
            else:
                return max_score[1][goal]


        else:
            if max_score[level][goal] == 0:
                max_score[2][goal] = DP(1, goal-1) + max_score[0][goal]
                return max_score[2][goal]
            else:
                return max_score[2][goal]

num = int(input())
score_list = [0]
max_score = [[0] * (num+1) for _ in range(3)]
for i in range(1, num+1):
    max_score[0][i] = int(input())

if num == 1:
    print(max_score[0][1])
else:
    max_score[1][1] = max_score[0][1]
    max_score[1][2] = max_score[0][2]
    max_score[2][2] = max_score[1][1] + max_score[0][2]

    print(max(DP(1, num), DP(2,num)))