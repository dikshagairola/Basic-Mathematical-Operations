#simple interest
#principal=float(input("Enter principal amount"))
#rate=float(input("Enter rate"))
#time=float(input("Enter time"))
#si=(principal*rate*time)/100
#print("simple interest is:",si)# #compund interest

principal= float(input("Enter the principal amount: "))
rate= float(input("Enter the rate"))
time= float(input("Enter the time"))
amount=principal*(1+rate/100)**time
ci=amount-principal
print("compound interest is", ci)


