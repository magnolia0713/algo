import sys
input = sys.stdin.readline
n, p = map(int, input().split())

stacks = [[] for _ in range(500001)]

cnt = 0
for _ in range(n):
    string, fret = map(int, input().split())

    while True:
        #손가락 여유가 없을 때
        if not stacks[string]:
            stacks[string].append(fret)
            cnt += 1
            break

        #치고자 하는 음이 더 높을 때
        if stacks[string][-1] < fret:
            stacks[string].append(fret)
            cnt += 1
            break

        # 치고자 하는 음이 더 낮을 때
        elif stacks[string][-1] > fret:
            stacks[string].pop()
            cnt += 1
        else:
            break

print(cnt)