number = int(input("Number: "))

if number % 3 == 0 and not number % 5 == 0:
    print("Fizz")
elif number % 5 == 0 and not number % 3 == 0:
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
