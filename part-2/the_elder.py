name_person_1 = input('Person 1: ')
age_person_1 = int(input('Age: '))
name_person_2 = input('Person 2: ')
age_person_2 = int(input('Age: '))

if age_person_1 > age_person_2:
    print(f'The elder is {name_person_1}')
elif age_person_2 > age_person_1:
    print(f'The elder is {name_person_2}')
else:
    print(f'{name_person_1} and {name_person_2} are the same age')
