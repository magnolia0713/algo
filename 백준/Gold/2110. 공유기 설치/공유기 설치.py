import sys
input = sys.stdin.readline

def find(start, end):

    if start == end:
        return start

    mid = (start + end) // 2

    if is_valid(mid+1):
        return find(mid+1, end)

    else:
        return find(start, mid)


def is_valid(key):
    cnt = 0
    tc = 0
    for i in range(1, n):
        cnt += nums[i]
        if cnt >= key:
            tc += 1
            cnt = 0

    if tc >= c-1:
        return True

    else:
        return False

n, c = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

end = (nums[-1] - nums[0]) // (c-1)


for i in range(n-1, 0, -1):
    nums[i] -=nums[i-1]
nums[0] = 0

result = find(0, 2 * end)

print(result)