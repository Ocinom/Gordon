weight = float(input('Enter your weight in kgs: '))
height = float(input('Enter your height in metres: '))
result = weight / (height**2)

print('Your BMI is {:.2f}'.format(result))