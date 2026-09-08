num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum = a**3 + b**3 + c**3

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
