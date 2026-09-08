n = int(input("Enter size: "))

# Top part
for i in range(n // 2):
    for j in range(n // 2 - i):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        print("*", end=" ")

    for j in range(n - 2 * i - 1):
        print(" ", end=" ")

    for j in range(2 * i + 1):
        print("*", end=" ")

    print()

# Bottom part
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
