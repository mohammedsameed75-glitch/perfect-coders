n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="  ")

    # Increasing alphabets
    for j in range(i):
        print(chr(65 + j), end=" ")

    # Decreasing alphabets
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end=" ")

    print()