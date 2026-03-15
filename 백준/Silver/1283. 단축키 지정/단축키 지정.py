import sys

input = sys.stdin.readline
T = int(input())
registered = set()
for _ in range(T):
    word = list(input().split())

    for i in range(len(word)):
        if word[i][0] not in registered:
            registered.add(word[i][0].upper())
            registered.add(word[i][0].lower())
            word[i] = '[' + word[i][0] + ']' + word[i][1:]
            break

    else:
        for i in range(len(word)):
            check = False
            for j in range(1, len(word[i])):
                if word[i][j] not in registered:
                    registered.add(word[i][j].upper())
                    registered.add(word[i][j].lower())
                    word[i] = word[i][:j] + '[' + word[i][j] + ']' + word[i][j+1:]
                    check = True
                    break

            if check:
                break

    print(' '.join(word))