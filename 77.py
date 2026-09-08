def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n, end=" ")
    print_numbers_decreasing(n - 1)


def print_numbers_decreasing(n):
    if n == 0:
        return

    print(n, end=" ")
    print_numbers_decreasing(n - 1)


n = int(input("Enter N: "))

print_numbers(n)
