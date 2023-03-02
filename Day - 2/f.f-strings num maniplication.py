#Number maniplucation

num = 2
print(num)

num += 5
print(num)

mul=4
mul *= 2# => mul = mul*2
#similarly you can use above method for all math operations like +,-,/,*,% etc.
print(mul)


height = 152.6
print(height)#floating value
print(round(height))#rounding value
print(int(height))#int value

#f-strings in python

score  = 2
name = 'rakesh'
age = 21
isWinner = True

#we can typecast each and every data-type using str().
#But using f-strings method we can easilly convert it into string.
#Result

print(f'My name is {name} and my age is {age}.')
print(f'I scored in a game {score} goals and i am the winner is {isWinner}')
