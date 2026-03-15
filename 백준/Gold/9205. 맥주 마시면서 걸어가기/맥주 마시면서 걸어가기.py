def bfs():
    stack = [start]
    while stack:
        r, c = stack.pop()
        if r == end_point[0] and c == end_point[1]:
            return 'happy'
        for n, m in conv_list:
            if abs(r-n) + abs(c-m) <= 1000 and [n,m] not in visited_list:
                stack.append([n,m])
                visited_list.append([n,m])
    return 'sad'
#=================================================================
T = int(input())
for tc in range(T):
    conv_num = int(input())
    start = list(map(int, input().split()))
    conv_list = []
    visited_list = []

    for _ in range(conv_num):
        i, j = map(int, input().split())
        conv_list.append([i,j])

    end_point = list(map(int, input().split()))
    conv_list.append(end_point)
    print(bfs())