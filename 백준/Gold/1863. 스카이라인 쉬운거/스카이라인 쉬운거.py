stack = [0]
cnt = 0
n = int(input())
for _ in range(n):
    index, num = map(int, input().split())
    if not stack:
        stack.append(num)
        cnt += 1

    else:
        while stack:
            if stack[-1] < num:
                stack.append(num)
                cnt += 1
                break

            elif stack[-1] == num:
                break

            else:
                stack.pop()

        else:
            stack.append(num)
            cnt += 1

print(cnt)
