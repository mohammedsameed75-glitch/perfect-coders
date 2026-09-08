cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit")
elif cp > sp:
    print("Loss")
else:
    print("No profit no loss")
