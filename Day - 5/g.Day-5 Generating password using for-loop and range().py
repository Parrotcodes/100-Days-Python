#Day -5
#Major Project - Generating Password
        #Easy level
        #Hard Level

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#','$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



print('Welcome to the PyPassword Generator!')
que = int(input('How many letters would you like in your password?'))
sym = int(input('How many symbols would you like?'))
num = int(input('How many numbers would you like?'))

#-----***Easy Level***---

#gerate_password = "dE$5^&3G%*"

gerate_password=''

for char in range(1,que+1):
        #random_char = random.choice(letters)
        gerate_password += random.choice(letters)

for symb in range(1,sym+1):
        gerate_password += random.choice(symbols)

for nums in range(1,num+1):
        gerate_password += random.choice(numbers)

print('')       
print(f'Here is your Easy Level sequential password:    {gerate_password}   ')


print('')
print('')


#------***Hard Level***-------


#appending char into list

new_password_list = []

for char in range(1,que+1):
        new_password_list.append(random.choice(letters))

for symb in range(1,sym+1):
        new_password_list+=random.choice(symbols)

for nums in range(1,num+1):
        new_password_list += random.choice(numbers)

print('')
print(new_password_list)
random.shuffle(new_password_list)#shuffle the password / list items
print('')
print(new_password_list)

password_list = ""

for char in new_password_list:
        password_list += char

print('')
print(f'Here is your Hard Level randomised password:  {password_list}  ')
