from collections import deque


def piing(word):

    idx = 0
    for i in range(1, n):
        while idx > 0 and word[idx] != word[i]:
            idx = pi[idx - 1]

        if word[idx] == word[i]:
            idx += 1
            pi[i] = idx
    return

def explosion():
    j = 0
    stack = []
    while word:

        p = word.popleft()
        stack.append(p)

        while j > 0 and p != pied[j]:
            j = pi[j - 1]

        if pied[j] == p:
            if j == n - 1:
                for _ in range(n):
                    stack.pop()
                j = 0
                p = min(n, len(stack))

                for _ in range(p):
                    temp = stack.pop()
                    word.appendleft(temp)
                j = 0
            else:
                j += 1

    return stack

word = deque(input())
m = len(word)
pied = list(input())
n = len(pied)
pi = [0] * n
piing(pied)
result = ''.join(explosion())
if not result:
    result = 'FRULA'
print(result)