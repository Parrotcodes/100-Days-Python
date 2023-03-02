#Type Error,Type Checking and Type Conversion

#combination of both string and numbers - TypeError 
num_char = len(input('Enter your name'))
#print('Your name contains '+num_char+' characters.')#Type Error - string concatinating with number is not possible.

#solution for this is Type conversion
new_num_char = str(len(input('Enter your name which is a string:')))
print('your name contains '+ new_num_char +' characters.')

#Integer type example
age = input('Enter your age:')
print('My age is '+ age +'.')


#Type conversions using Data Types
a = 123
print(type(a))#int

a = str(123)#string
print(type(a))

num = float(10)#int -> float
print(type(num))

#comibing sting and num converisions
print(70+int('100'))
print(str(123)+str(100))

