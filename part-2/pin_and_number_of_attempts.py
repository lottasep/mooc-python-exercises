attempts = 0

while True:
    pin = input("PIN: ")
    attempts += 1

    if pin == "4321":
        success = True
        break

    print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
