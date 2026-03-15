from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = ''.join(map(str, arr))
target = ''.join(map(str, sorted(arr)))

# 이미 정렬됨
if start == target:
    print(0)
    exit()

visited = set()
visited.add(start)

q = deque()
q.append((start, 0))

while q:
    state, cnt = q.popleft()

    # 문자열을 리스트로 변환
    state_list = list(state)

    for i in range(n - k + 1):
        # 길이 k 구간 뒤집기
        new_list = state_list[:]
        new_list[i:i+k] = reversed(new_list[i:i+k])
        new_state = ''.join(new_list)

        if new_state == target:
            print(cnt + 1)
            exit()

        if new_state not in visited:
            visited.add(new_state)
            q.append((new_state, cnt + 1))

print(-1)
