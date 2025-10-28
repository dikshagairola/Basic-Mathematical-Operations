principal= float(input("Enter the principal amount: "))
rate= float(input("Enter the rate"))
time= float(input("Enter the time"))
amount=principal*(1+rate/100)**time
ci=amount-principal
print("compound interest is", ci)

