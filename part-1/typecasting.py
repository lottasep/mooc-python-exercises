'''
Please write a program which asks the user for a floating point number
and then prints out the integer part and the decimal part separately.
Use the Python int function.

You can assume the number given by the user is always greater than zero.
'''

number = float(input('Please type in a number: '))
print(f'Integer part: {int(number)}')
print(f'Decimal part: {number - int(number)}')