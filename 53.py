def product_digits(num):
    if num < 10:
        return num
    return (num % 10) * product_digits(num // 10)

num = int(input("Enter a number: "))

print("Product of digits =", product_digits(num))
