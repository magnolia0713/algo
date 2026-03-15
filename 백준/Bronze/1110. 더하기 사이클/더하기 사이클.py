def digits_sum(number):
    if number < 10:
        return number
    else:
        return number % 10 + digits_sum(number//10)
        
global trial_number

N = int(input())
A = N % 10
B = digits_sum(N) % 10

M = A * 10 + B

trial_number = 1

while M != N:
    A = M % 10
    B = digits_sum(M) % 10
    M = A * 10 + B
    
    trial_number += 1

print(trial_number)