word_a = input()

word_A = list(word_a.upper())

list_alphabet = ['A','B','C','D','E','F','G','H','I','J','K',
'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

max_t = 0

for i in list_alphabet:
    t = word_A.count(i)
    if t > max_t:
        max_t = t
        K = i
    elif t == max_t:
        K = '?'
    
print(K)