value = int(input("Value of gift: "))

if value < 5000:
    print("No tax!")
else:
    if value < 25000:
        tax = 100 + (value - 5000) * 0.08
    elif value < 55000:
        tax = 1700 + (value - 25000) * 0.10
    elif value < 200000:
        tax = 4700 + (value - 55000) * 0.12
    elif value < 1000000:
        tax = 22100 + (value - 200000) * 0.15
    else:
        tax = 142100 + (value - 1000000) * 0.17
    print(f"Amount of tax: {tax:.2f} euros") # printtaa 2 desimaalia f-stringissä, esim: If tax = 123.456789 → f"{tax:.2f}" would give "123.46" (rounded!)



'''
Formatting numbers to 2 decimal places:

Option 1: Using an f-string (recommended for printing)
print(f"Amount of tax: {tax:.2f} euros")
# Example: if tax = 123.456789 → prints "Amount of tax: 123.46 euros" (rounded)

Option 2: Keep the value rounded as a number for calculations
tax_decimal = round(tax, 2)
print("Amount of tax: " + str(tax_decimal) + " euros")

Option 3: Create a formatted string using .format() (older style)
tax_decimal = "{:.2f}".format(tax)
print("Amount of tax: " + tax_decimal + " euros")
'''

