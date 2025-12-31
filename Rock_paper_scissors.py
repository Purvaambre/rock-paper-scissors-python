

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
user_input = int(input("What do you want to choose? Type 0 for Rock , 1 for Paper or 2 for Scissors\n"))
#user_input is coming from input(), which always returns a string


if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("You typed an invalid number. You lose!")
    exit() # stop the program here if invalid


print("Computer chose:")

import random
response = random.randint(0, 2)

if response == 0:
    print(rock)
elif response == 1:
    print(paper)
else:
    print(scissors)

# Decide winner
if user_input == response:
    print("It's a draw!")
elif (user_input == 0 and response == 2) or (user_input == 1 and response == 0) or (user_input == 2 and response == 1):
    print("You win!")
else:
    print("You lose!")
