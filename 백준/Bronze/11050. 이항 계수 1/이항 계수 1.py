N, K = map(int,input().split())

final_number = 1

for i in range (N, N-K, -1):
    final_number *= i
    final_number /= N-i+1

print(int(final_number))