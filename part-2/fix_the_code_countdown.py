number = 5
print("Countdown!")
while number > 0:
    print(number)
    number -= 1
print("Now!")

'''
Ensimmäinen mieleen tullut ratkaisu, ei niin hyvä:

number = 6
print("Countdown!")
while True:
  number = number - 1
  print(number)
  if number < 2:
    break

print("Now!")

'''
