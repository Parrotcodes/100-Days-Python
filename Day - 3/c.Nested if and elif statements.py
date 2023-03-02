#Program for Nested if statements and elif statements

print('This program is created using Nested if and elif statements')

#Nested if-else statements

height = int(input('Enter your height in cm:'))

if height >120:
    print('your eligible to ride')
    age=int(input('What is your age?'))
    if age<=18:
        print('Please pay $7.')
    else:
        print('please pay $12.')
else:
    print('Invalid height! sorry,You can not ride')


#   ---***---  #

#elif statements

height2 = int(input('Enter your height in cm:'))

if height2 >120:
    print('your eligible to ride')
    age2=int(input('What is your age?'))
    if age2 <12:
        print('Please pay $5.')
    elif age2<=18:
        print('Please pay $7.')
    else:
        print('please pay $12.')
else:
    print('Invalid height! sorry,You can not ride')


#   ---***---  #
