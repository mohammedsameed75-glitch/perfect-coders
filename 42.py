marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if marks >= 75 and attendance >= 75 and income <= 250000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")
