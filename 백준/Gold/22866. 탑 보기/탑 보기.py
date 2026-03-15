from collections import deque

n = int(input())
n_list = [0] + list(map(int, input().split()))

stack = [(1, n_list[1])]
memo = [[0,100000] for _ in range(n+1)]

#순방향
for i in range(2, n+1):
    if n_list[i] < n_list[i-1]:
        memo[i][0] += len(stack)
        memo[i][1] = stack[-1][0]
        stack.append((i, n_list[i]))

    else:
        while stack:
            if stack[-1][1] <= n_list[i]:
                stack.pop()


            else:
                memo[i][0] += len(stack)
                memo[i][1] = stack[-1][0]
                stack.append((i, n_list[i]))
                break

        else:
            stack.append((i, n_list[i]))

stack = [(n, n_list[n])]
#역방향
for i in range(n-1, 0, -1):
    if n_list[i] < n_list[i+1]:
        memo[i][0] += len(stack)

        if memo[i][1] != 100000:
            if i - memo[i][1] > stack[-1][0] - i:
                memo[i][1] = stack[-1][0]
        else:
            memo[i][1] = stack[-1][0]

        stack.append((i, n_list[i]))

    else:
        while stack:
            if stack[-1][1] <= n_list[i]:
                i, stack.pop()


            else:
                memo[i][0] += len(stack)

                if memo[i][1] != 100000:
                    if i - memo[i][1] > stack[-1][0] - i:
                        memo[i][1] = stack[-1][0]
                else:
                    memo[i][1] = stack[-1][0]

                stack.append((i, n_list[i]))
                break

        else:
            stack.append((i, n_list[i]))


for a, b in memo[1:]:
    if a:
        print(a,b)
    else:
        print(a)
