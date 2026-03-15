import sys
N, M = map(int, input().split())
word_dict = {}
for _ in range(N):
    word = sys.stdin.readline()
    if len(word) > M:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
#print(word_dict)
word_list = []

for key, value in word_dict.items():
    word_list.append([key, value, len(key)])

#print(word_list)
word_list.sort(key = lambda x: (-x[1], -x[2], x[0]))

for word in word_list:
    sys.stdout.write(''.join(word[0]))