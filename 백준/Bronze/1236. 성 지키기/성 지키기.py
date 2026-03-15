N, M = map(int,input().split())

matrix = list(list(input()) for _ in range(N))

transposed_m = list(list(zip(*matrix)))


bouncer_a = 0

bouncer_b = 0

for i in range(N):
    if matrix[i].count('X') == 0:
        bouncer_a += 1


for i in range(M):
    if transposed_m[i].count('X') == 0:
        bouncer_b += 1

if bouncer_a >= bouncer_b:
    bouncer = bouncer_a

else:
    bouncer = bouncer_b

print(bouncer)