#BMI Calculator using Nested if-else elif statements

print('Calculator for BMI and giving the suggestions')

height = input('Enter your heignt in m:')
weight = input('Enter your weight in kg: ')

#logic for BMI
BMI = int(weight) / float(height)**2

print('Exact number:',int(BMI))
#BMI = 20

if BMI < 18.5:
    print(f'your BMI is {BMI},You are Underweight')
elif BMI < 25:
    print(f'your BMI is {BMI},you are normal weight')
elif BMI <30:
    print(f'your BMI is {BMI},you are overweight')
elif BMI <35:
    print(f'your BMI is {BMI},you are obesity')
else:
    print(f'your BMI is {BMI}, You are clinically obes')
