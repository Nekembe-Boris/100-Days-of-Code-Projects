import random

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

game_list =[rock, paper, scissors]

choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if choice < 0 or choice > 2:
    print("You entered a wrong number. Please enter a valid number")
else:
    print(f"You chose \n{game_list[choice]}")

random_int = random.randrange(0, 2)
print(f"The computer chose \n{game_list[random_int]}")

if choice == random_int:
    print("There is a draw!")
elif (choice == 0) and (random_int == 2):
    print("You won!")
elif (choice == 2) and (random_int == 1):
    print("You won!")
elif (choice == 1) and (random_int == 0):
    print("You won!")
else:
    print("You lose")
