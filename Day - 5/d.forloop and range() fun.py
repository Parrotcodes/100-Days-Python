#For-loop and range() function in python

print('This is range() function for selecting range of numbers')
for num in range(1,11):
    print(num)

print('This is jumping or step-forwarding concept (1,30,->2)')
#jumps step forward to 2-steps  
for num2 in range(1,21,2):
    print(num2)

#sum of 100 numers

total = 0
for i in range(1,101):
    total += i

print(f'The sum of 1-100 number is {total}')
