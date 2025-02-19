import math

students = int(input('How many students on the course? '))
group_size = int(input('Desired group size? '))

print(f'Number of groups formed: {math.ceil(students / group_size)}')