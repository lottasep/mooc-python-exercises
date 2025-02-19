lunches = int(input('How many times a week do you eat at the student cafeteria? '))
lunch_price = float(input('The price of a typical student lunch? '))
groceries_price = float(input('How much money do you spend on groceries in a week? '))

avg_lunches = lunches * lunch_price / 7
avg_groceries = groceries_price / 7

print('Average food expenditure:')
print(f'Daily: {avg_lunches + avg_groceries} euros')
print(f'Weekly: {lunches * lunch_price + groceries_price} euros')