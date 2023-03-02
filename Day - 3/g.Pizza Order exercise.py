#Pizza Order Practicing Excersice program

print('Welcome to Python Pizza Deliveries!')

#See menu card
print('--- Menu Card ---')

print('Small Pizza: $15')
print('Medium Pizza: $20')
print('Large Pizza: $25')
print('\n')
print('Pepperoni for small Pizza: +$2')
print('Pepperoni for Medium or Large Pizza: $3')
print('\n')
print('Extra cheese for any size of pizza: $1')
print('\n')

size = input('What size pizza do you want? small(S),Medium(M),Large(L):')
add_pepperoni = input('Do you want pepperoni?')
extra_cheese = input('Do you want extra cheese?')

bill = 0

#Size of Pizza
if size=='S':
    bill += 15
elif size =='M':
    bill +=20
else:
    bill += 25

#add pepperoni
if add_pepperoni == 'Y':
    if size == 'S':
        bill +=2
    else:
        bill += 3

#extra cheese
if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is ${bill}.')
