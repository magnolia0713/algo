word_set = set()

N, M = map(int, input().split())

for _ in range(N):
    word = input()
    word_set.add(word)

count = 0
for _ in range(M):
    word = input()
    if word in word_set:
        count += 1
print(count)
