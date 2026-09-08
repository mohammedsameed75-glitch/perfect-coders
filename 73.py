count = 0
total = 0

while True:
    num = float(input("Enter a number (-1 to stop): "))

    if num == -1:
        break

    total = total + num
    count = count + 1

if count > 0:
    average = total / count
    print("Count =", count)
    print("Average =", average)
else:
    print("No numbers entered")
