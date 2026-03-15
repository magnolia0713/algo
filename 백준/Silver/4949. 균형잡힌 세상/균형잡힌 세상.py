
while True:
    
    dialog = input()
    
    if dialog == '.':
        break
        
    #print(dialog)
    stack = []
    for i in dialog:
        if i == '(' or i == '[':
            stack.append(i)
            #print(stack)

        elif i == ')' or i == ']':
            if stack:
                if i == ')':
                    if stack.pop() != '(':
                        print('no')
                        break

                else:
                    if stack.pop() != '[':
                        print('no')
                        break
            else:
                print('no')
                break
    else:
        if stack:
            print('no')

        else:
            print('yes')