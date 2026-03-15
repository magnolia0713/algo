T = int(input())
point = 0

for _ in range(T):
    
    word = list(input())
    set_alphabet = set()
    restored = 0
    for alphabet in word:
        if alphabet == restored:
            continue
        elif alphabet in set_alphabet:
            break
        else:
            set_alphabet.add(alphabet)
            restored = alphabet

    else: point += 1

print(point)