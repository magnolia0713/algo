#from collections import deque
import sys
n = int(input())
word = input()
input = sys.stdin.readline
#word를 indexing할 변수 counter
final_word = [word[0]]

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

#print(tree)

basket = [1]
candidate = []
word_candidate = []
#print(basket)
visited = [0] * (n+1)
visited[1] = 1

while basket:
    candidate.clear()
    word_candidate.clear()
    a_max = 0

    # 트리의 깊이마다 candidate 생성
    for _ in range(len(basket)):
        node = basket.pop()
        for i in tree[node]:
            if not visited[i]:
                visited[i] = 1
                candidate.append(i)

    # candidate의 value 측정
    
    for i in candidate:
        temp = word[i-1]
        if a_max < ord(temp):
            word_candidate.clear()
            word_candidate.append(i)
            a_max = ord(temp)
        elif a_max == ord(temp):
            word_candidate.append(i)

    if candidate:
        final_word.append(word[word_candidate[0]-1])

    basket.extend(word_candidate)

print(''.join(final_word))