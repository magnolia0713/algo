import sys
input = sys.stdin.readline
while True:
    pages = int(input())

    # 입력의 끝이면 프로그램 종료
    if not pages:
        break

    visited = [0] * (pages+1)
    orders = list(input().split(','))
    #print(orders)
    for i in orders:
        num = list(map(int, i.split('-')))

        # 한 장만 입력일 때
        if len(num) == 1:
            if num[0] <= pages:
                visited[num[0]] = 1

        # 두 장 이상 연속으로 입력될 때

        else:
            if num[1] > pages:
                num[1] = pages

            for page in range(num[0], num[1]+1):
                visited[page] = 1

    print(sum(visited))