# deque을 쓰자.
import sys
from collections import deque
input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    n = int(input())
    word = list(input().split())

    new_word = deque()
    new_word.append(word[0])

    for i in range(1, n):

        # 문자열 순위가 같거나 더 크다면 앞에, 작다면 뒤에
        if new_word[0] >= word[i]:
            new_word.appendleft(word[i])

        else:
            new_word.append(word[i])

    print(''.join(new_word))