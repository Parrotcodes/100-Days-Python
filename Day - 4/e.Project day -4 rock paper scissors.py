#Day-4 Project
#Topic - Rock Paper Scissors

import random

print('Welcome to the ROCK PAPER SCISSORS Game studio!')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_icons = [rock,paper,scissors]

user_choice = int(input('What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(user_choice)
print(game_icons[user_choice])#print the hand-icon

#user conditon
if user_choice >=3 and user_choice<0:
    print('You typed an invalid number, You lose!')
else:
    #computer choice and conditions between both
    computer_choice = random.randint(0,2)
    print(computer_choice)#print random number
    print(game_icons[computer_choice])#print the hand-icon

    if user_choice==0 and computer_choice == 2:
        print('You win!')
    elif computer_choice==0 and user_choice==2:
        print('Computer win!')
    elif computer_choice>user_choice:
        print('Computer win!')
    elif user_choice>computer_choice:
        print('You win!')
    elif user_choice==computer_choice:
        print('Your Game is draw!')
   
        
