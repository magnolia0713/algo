total_score = 0

def abs(number):
    if number < 0:
        number = number * -1
    
    return number


while True :
    try:
        score = int(input())
        if abs(total_score - 100) < abs(total_score + score - 100):
            break
        else:
            total_score += score
    except:
        break
print(total_score)