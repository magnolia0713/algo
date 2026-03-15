a, b, c = map(int, input().split())

class calculator:
    def one(A,B,C):
        return (A+B)%C
    def two(A,B,C):
        return ((A%C) + (B%C))%C
    def three(A,B,C):
        return (A * B)%C
    def four(A,B,C):
        return ((A%C) * (B%C))%C

print(calculator.one(a, b, c))
print(calculator.two(a, b, c))
print(calculator.three(a, b, c))
print(calculator.four(a, b, c))