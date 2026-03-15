import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

for t in targets:
    # bisect_left는 정렬된 배열에서 t가 들어갈 수 있는 가장 왼쪽 인덱스를 반환
    idx = bisect.bisect_left(A, t)
    # idx가 배열 길이보다 작고, 그 위치의 값이 t와 같으면 존재함
    if idx < N and A[idx] == t:
        print(1)
    else:
        print(0)