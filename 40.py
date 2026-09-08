balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum_balance = float(input("Enter minimum balance: "))

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount + minimum_balance <= balance:
    balance = balance - amount
    print("Withdrawal Approved")
    print("Remaining Balance =", balance)
else:
    print("Withdrawal Rejected")
