#Find year your choosen is Leap year or not

year = int(input('Enter any year:'))

#using Nested if-else statement
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('Leap year')
        else:
            print('Not a Leap year')
    else:
        print('Leap year')
else:
    print('Not a Leap Year')




#High level thinking method and easy process to find leap year or not
'''
if ((year%4==0) or (( year%100==0)and (year%100!=0))):
    print('Leap year')
else :
    print('Not a Leap year')
'''

