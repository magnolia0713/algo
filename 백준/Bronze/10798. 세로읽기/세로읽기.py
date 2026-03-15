matrix_a = list(list(input()) for _ in range(5))


A = max(
    len(matrix_a[0]),
    len(matrix_a[1]),
    len(matrix_a[2]),
    len(matrix_a[3]),
    len(matrix_a[4])
)

list_word = []

for i in range(A):
    for j in range(5):
        try:
            list_word += matrix_a[j][i]

        except :
            continue

print(''.join(list_word))