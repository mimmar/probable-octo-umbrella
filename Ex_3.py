'''
height = float(input('Please enter your height in metres: '))
weight = float(input('Please enter your weight in kgs: '))

bmi = round(weight / height ** 2, 1)
bmi_scale = ['underweight', 'normal weight', 'overweight', 'obese']

if bmi <= 18.5:
    bmi_scale = [bmi_scale[0]]
elif bmi <= 24.9:
    bmi_scale = [bmi_scale[1]]
elif bmi <= 29.9:
    bmi_scale = [bmi_scale[2]]
else:
    bmi_scale = [bmi_scale[3]]

print(f'Your BMI is : {bmi}, you are {bmi_scale[0]}')
'''

def convert_cm_to_m(cm):
    return cm / 100

height = input('Please enter your height: ')
try:
    height = float(height)
except ValueError:
    print('Invalid height. Please enter a number.')

if height < 2.5:
    height_m = height
    height_unit = 'm'
else:
    height_cm = height
    height_m = convert_cm_to_m(height_cm)
    height_unit = 'cm'

weight = float(input('Please enter your weight in kgs: '))

bmi = round(weight / height_m ** 2, 1)
bmi_scale = ['underweight', 'normal weight', 'overweight', 'obese']

if bmi <= 18.5:
    bmi_scale = bmi_scale[0]
elif bmi <= 24.9:
    bmi_scale = bmi_scale[1]
elif bmi <= 29.9:
    bmi_scale = bmi_scale[2]
else:
    bmi_scale = bmi_scale[3]

print(f'Height: {height:.2f}{height_unit}, Weight: {weight:.1f}kg, BMI: {bmi:.1f}, Category: {bmi_scale}')
