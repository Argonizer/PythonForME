
annual_rate = float(input("Enter Yearly Interest Rate\n"))
monthly_rate = annual_rate/1200

years = int(input("Enter number of years, for example 5: \n"))
loan_amount = float(input("Enter loan amount, example 120000.95 \n"))

EMI = loan_amount * monthly_rate / (1 - 1/(1 + monthly_rate)**(years*12))
total_payment = EMI * years * 12

print("The monthly payment is", EMI)
print("The total payment is", total_payment)