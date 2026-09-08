n = int(input("Enter size: "))

for i in range(n):
    if i <= n // 2:
        spaces = 2 * i
    else:
        spaces = 2 * (n - i - 1)

    for j in range(n):
        if j == 0 or j == n - 1:
            print("*", end=" ")
        elif j == spaces // 2 + 1 or j == n - spaces // 2 - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

