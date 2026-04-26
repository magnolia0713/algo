import sys

# wellknown 문제
input = sys.stdin.readline
INF = 1e8

n = int(input())
students = [[0, 0, 0] for _ in range(n + 1)]

# 등수 입력
for exam in range(3):
    rank_list = list(map(int, input().split()))
    for rank, student_id in enumerate(rank_list, 1):
        students[student_id][exam] = rank

# 오름차순 정렬
sorted_students = sorted(students[1:], key=lambda x: x[0])

tree = [INF] * (2 * n)

def update(idx, val):
    idx -= 1
    idx += n  # 리프 노드의 시작 위치로 이동
    tree[idx] = val
    while idx > 1:
        idx //= 2
        tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])

def query(left, right):
    # left/right도 0-based로 변환
    left -= 1
    right -= 1
    left += n
    right += n

    result = INF
    while left <= right:
        if left % 2 == 1:
            result = min(result, tree[left])
            left += 1
        if right % 2 == 0:
            result = min(result, tree[right])
            right -= 1
        left //= 2
        right //= 2
    return result

awesome_count = 0

# 1차 시험 성적이 가장 좋은 학생부터 순차적으로 검사
for score1, score2, score3 in sorted_students:
    best_score3 = INF

    # 나보다 1차 시험을 잘 본 학생들 중 2차 시험도 나보다 잘 본 구간의 3차 시험 최고 등수를 쿼리
    if score2 > 1:
        best_score3 = query(1, score2 - 1)

    # 그 최고 등수가 내 3차 시험 등수보다 뒤쳐진다면 나를 3과목 모두 압도하는 학생은 존재하지 않음
    if best_score3 > score3:
        awesome_count += 1

    # 세그먼트 트리의 내 2차 등수 위치에 내 3차 등수 업데이트
    update(score2, score3)

print(awesome_count)
