#BMI Calculator (Body Mass Index)

#Formulae BMI = Weight(kg) / height**2(m**2)

print('Calculate your BMI value:')

w = input('Weight in kg:')
h = input('Height in m:')

BMI = int(w) / float(h)**2

print(BMI)#float
print('Exact number:',int(BMI))
