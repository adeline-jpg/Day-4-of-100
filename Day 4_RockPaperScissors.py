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

import random
images = [rock, paper, scissors]
user_input = int((input("what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n")))

if user_input <= 2 and user_input >= 0: #they know the order of the options already since they order in the lists matter!
    print(images[user_input]) #syntax confused me here
else:
    print("you've got the wrong inputs!") #in case other inputs that are not 0, 1, 2 are inputted.

computer_input = int(random.randint(0,2)) #confusion -- forgot to change the type, so kept getting a type error.
print(f"Computer Chose: {images[computer_input]}") #syntax is list[variable]
if user_input == 2 and computer_input == 0: #tip -- put the user input first since it reads left to right, and the first input is user and not computer.
    print("you lose")
elif user_input == 0 and computer_input == 2: #order of if else statements matter too! if this was the last if statement, i would have won even if these were the same results.
    print("you lose")
elif user_input > computer_input:
    print("you win")
elif user_input < computer_input:
    print("you lose")
elif user_input == computer_input:
    print("it's a draw!")