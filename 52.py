num = int(input("Enter a number: "))

while num != 1 and num != 4:
    sum = 0

    while num != 0:
        digit = num % 10
        sum = sum + digit ** 2
        num = num // 10

    num = sum

if num == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
