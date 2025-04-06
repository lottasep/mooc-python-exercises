year = int(input("Year: "))
next_leap_year = year + 1


while True:
    if (next_leap_year % 4 == 0 and next_leap_year % 100 != 0) or (next_leap_year % 4 == 0 and next_leap_year % 100 == 0 and next_leap_year % 400 == 0):
        break
    else:
        next_leap_year += 1

print(f"The next leap year after {year} is {next_leap_year}")


