a, b = map(int, input().split())

class calculator:
    def add(a,b):
        return a + b
    
    def min(a,b):
        return a - b
    
    def mul(a,b):
        return a * b
    
    def div(a,b):
        return a // b

    def rem(a,b):
        return a % b

print(calculator.add(a,b))

print(calculator.min(a,b))

print(calculator.mul(a,b))

print(calculator.div(a,b))

print(calculator.rem(a,b))