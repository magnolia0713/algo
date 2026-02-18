import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

# union_find
team_leader = [i for i in range(n+1)]

def leader(node):
    if team_leader[node] != node:
        team_leader[node] = leader(team_leader[node])

    return team_leader[node]

def union(node1, node2):
    team_leader[leader(node2)] = leader(node1)
    return

#print(team_leader)

line_list = []
for _ in range(m):
    line_list.append(list(map(int, input().split())))

line_list.sort(key=lambda x:x[2])
#print(line_list)

ans = 0
cnt = 0
n -= 1
for s, e, w in line_list:
    if leader(s) != leader(e):
        union(s, e)
        ans += w; cnt += 1
        #print(team_leader, ans)
        if cnt == n:
            break

print(ans)


