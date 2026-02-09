word = input().strip()
result = []

for ch in word:
    if 65 <= ord(ch) <= 90:  
        result.append(chr(ord(ch) + 32))
    else:                      
        result.append(chr(ord(ch) - 32))

print("".join(result))
