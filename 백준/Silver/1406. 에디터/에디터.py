import sys
input = sys.stdin.readline

word_list = list(input().strip())
stack = []
n = int(input())
pointer = len(word_list) - 1
for _ in range(n):
    order = input().split()
    if order[0] == 'L':
        if len(word_list):
            key = word_list.pop()
            stack.append(key)

    elif order[0] == 'D':
        if stack:
            key = stack.pop()
            word_list.append(key)

    elif order[0] == 'B':
        if len(word_list):
            word_list.pop()
            
    elif order[0] == 'P':
        word_list.append(order[1])

while stack:
    word_list.append(stack.pop())

print(''.join(word_list))