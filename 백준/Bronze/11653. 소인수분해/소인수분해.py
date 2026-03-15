N = int(input())

if N == 1:
    print()

else:
    list_factor = []

    def prime_factorizing(N):
        global list_factor

        for i in range(2, int(N ** 0.5 + 1)):
            if N % i == 0:
                k = N // i
                list_factor.append(i)
                return prime_factorizing(k)
    
        list_factor.append(N)
        return

    prime_factorizing(N)

    print(*list_factor, sep = '\n')