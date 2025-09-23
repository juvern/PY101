def prompt(message):
    print(f'=> {message}')

prompt('Enter the length')
length = input()

prompt('Enter the width')
width = input()

area_sqm = float(length) * float(width)
area_sqf = area_sqm * 10.7639

print(f'The room\'s area is {area_sqm:.2f} square meters or {area_sqf:.2f} square feet')