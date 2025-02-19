hourly_wage = float(input('Hourly wage: '))
hours_worked = int(input('Hours worked: '))
day_of_the_week = input('Day of the week: ')

if day_of_the_week == 'Sunday':
    print(f'Daily wages: {2 * hourly_wage * hours_worked} euros')
else:
    print(f'Daily wages: {hourly_wage * hours_worked} euros')