n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + (1 / i)

print("Sum =", sum)