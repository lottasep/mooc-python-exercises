year = int(input("Please type in a year: "))

if not year % 4 == 0:
    print("That year is not a leap year.")
elif year % 4 == 0 and year % 100 == 0 and not year % 400 == 0:
    print("That year is not a leap year.")
else:
    print ("That year is a leap year.")