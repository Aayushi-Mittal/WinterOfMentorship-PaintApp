p = int(input("Enter Principal: ") )
r = int(input("Enter Rate of Interest: ") )
t = int(input("Enter Time Period (in years): ") )
i = p*((1+r)**t)
print(f"Compound Interest = {i}")