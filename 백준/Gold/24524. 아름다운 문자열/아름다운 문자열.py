
word_list = input()
sub_word = input()
pointer = [-1] * len(sub_word)
cnt = 0
flag = False
while pointer[0] < len(word_list):

    for i in range(len(sub_word)):
        if i >= 1:
            if pointer[i] < pointer[i-1]:
                pointer[i] = pointer[i-1]

        pointer[i] += 1
        while pointer[i] < len(word_list):
            if word_list[pointer[i]] == sub_word[i]:
                #print(i,pointer[i])
                break
            pointer[i] += 1

        if pointer[i] >= len(word_list):
            flag = True
            break

    if flag:
        break
    else:
        cnt += 1

print(cnt)