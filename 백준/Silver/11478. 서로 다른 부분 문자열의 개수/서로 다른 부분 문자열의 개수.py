word = input()

memo = [set() for _ in range(len(word))]
cnt = 0
for subword_len in range(1, len(word)):
    for idx in range(len(word) - subword_len + 1):
        memo[subword_len].add(word[idx:(idx + subword_len)])

    cnt += len(memo[subword_len])

print(cnt+1)