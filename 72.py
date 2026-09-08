binary = int(input("Enter a binary number: "))

decimal = 0
power = 0

while binary != 0:
    digit = binary % 10
    decimal = decimal + digit * (2 ** power)
    power = power + 1
    binary = binary // 10

print("Decimal =", decimal)

