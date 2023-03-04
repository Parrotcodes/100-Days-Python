#Sum of all even numbers from 1-100

#Method-1 using range()

print('Method-1 using range()')
total=0
for eve in range(2,101,2):
    print(eve)
    total += eve

print(f'The sum of al the even numbers from 1 to 100 is {total}')

#Method-2 using if statement

print('Method-2 using if statement')
total2 = 0
for num in range(1,101):
    if num%2==0:
        total2 += num


print(total2)
