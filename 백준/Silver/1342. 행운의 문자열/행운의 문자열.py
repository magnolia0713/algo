from collections import Counter

def dfs(depth, lucky_word):

    global tt

    if depth == word_len:
        tt += 1
        return

    for i in range(len(word_arr)):
        if lucky_word[-1] != word_arr[i]:
            temp = word_arr.pop(i)
            dfs(depth+1, lucky_word + temp)
            word_arr.insert(i, temp)

tt = 0
word_arr = list(input())
word_len = len(word_arr)

for i in range(len(word_arr)):
    temp = word_arr.pop(i)
    dfs(1,temp)
    word_arr.insert(i, temp)

counter = Counter(word_arr)
for i in counter.values():
    for j in range(i, 1, -1):
        tt //= j
print(tt)

