word = input()
n = len(word)
string = []

for i in range(n-2):
    for j in range(i+1, n-1):
        string.append(word[i::-1] + word[j:i:-1] + word[n-1:j:-1])

string.sort()
print(string[0])