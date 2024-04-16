# Project: 01
# File:    05_formatString.py
# Author:  zavorszky@yahoo.com

age = 66
txt = "My name is Stephen, I am " + str(age)
print(txt)

txt2 = f"My name is Stephen, I am {age}"
print(txt2)

capitalFund = 100000
rateOfInterest = 12.6
txt3 = f"Current capital fund: {capitalFund:.2f} Ft"
txt3b = f"Current interest rate: {rateOfInterest:.2f} %"

print(txt3, ', ', txt3b)

txt4 = f"Current interest: {(capitalFund * rateOfInterest):.2f} Ft"
print(txt4)
