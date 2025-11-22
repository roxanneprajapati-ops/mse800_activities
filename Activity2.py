#Ask for the hours worked
HoursWorked = float(input("Enter Hours Worked"))
#Ask for pay rate
HoursPayRate = float(input("Enter Hours Pay Rate"))

#Comput gross pay
GrossPay = HoursWorked * HoursPayRate
print("Gross Income is ", GrossPay)

# Apply NZ income tax brackets
if GrossPay <= 15600:
    taxRate = 0.105

elif GrossPay <= 53500:
    taxRate = 0.175

elif GrossPay <= 78100:
    taxRate = 0.30

elif GrossPay <= 180000:
    taxRate = 0.33

else:
    taxRate = 0.39

# Calculate tax amount
taxAmount = GrossPay * taxRate
netIncome = GrossPay - taxAmount

print("Tax Rate:", taxRate)
print("Tax Amount:", taxAmount)
print("Net Income:", netIncome)