day, night, length = map(int, input().split())

time_a = (length - day) // (day - night)

is_real = (length - day) % (day - night)

if is_real != 0:
    time_a += 1
print(time_a + 1)