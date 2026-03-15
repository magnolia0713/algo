def bfs():
    #스타트로 시작: 스택이 아니라 큐
    stack = [start]
    while stack:
        r, c = stack.pop()

        #도착 발생시
        if r == end_point[0] and c == end_point[1]:
            return 'happy'

        #
        for n, m in conv_list:
            if abs(r-n) + abs(c-m) <= 1000 and [n,m] not in visited_list:
                stack.append([n,m])
                visited_list.append([n,m])

    #탐색 실패시
    return 'sad'

#=================================================================

# 정보 입력

T = int(input())
for tc in range(T):
    conv_num = int(input())
    start = list(map(int, input().split()))

    #편의점 좌표 저장소 ( -> 세트가 나은거같음: for문이 돌아간다던데?)
    conv_list = []

    # 방문좌표 기록, 마찬가지 set구현이 나은듯?
    visited_list = []

    # 편의점 좌표 저장소에 입력
    for _ in range(conv_num):
        i, j = map(int, input().split())
        conv_list.append([i,j])

    # 생각하기가 힘들어서 그냥 편의점 안에 넣음... 넣어도 문제는 없어보임
    end_point = list(map(int, input().split()))
    conv_list.append(end_point)
    print(bfs())