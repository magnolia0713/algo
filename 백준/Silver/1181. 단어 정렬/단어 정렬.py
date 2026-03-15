#리스트 목록 만들기
T = int(input())
list_word = []
for _ in range(T):
    word = input()
    list_word.append(word)
    
list_word.sort(key=lambda x : len(x))

# 갯수 정렬까지 ok

len_a = len(list_word[0])
marked = 0
# 사전 순 정렬

for i in range(1,T):
    if len(list_word[i]) == len_a:
        continue
    else:
        for num in range(len(list_word[marked])-1,-1,-1):
            list_word[marked:i] = sorted(list_word[marked:i], key=lambda x : x[num])
        marked = i
        len_a = len(list_word[i])
  
for num in range(len(list_word[marked])-1,-1,-1):
    list_word[marked:] = sorted(list_word[marked:], key=lambda x : x[num])
        
        
sort_a = list(dict.fromkeys(list_word))

print('\n'.join(sort_a))