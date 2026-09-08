n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum - i
    else:
        sum = sum + i

print("Sum =", sum)
