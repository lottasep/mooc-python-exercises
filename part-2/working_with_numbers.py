numbers = 0
sum = 0
mean = 0
positives = []
negatives = []

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    elif number >=0:
        positives.append(number)
    else:
        negatives.append(number)
    numbers += 1
    sum += number
    mean = sum / numbers

print(f"Numbers typed in {numbers}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {len(positives)}")
print(f"Negative numbers {len(negatives)}")