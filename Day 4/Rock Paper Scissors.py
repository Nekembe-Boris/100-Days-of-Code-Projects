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

choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))


sign = "Any"

if choice == 0:
    sign = rock
elif choice == 1:
    sign = paper
elif choice == 2:
    sign = scissors
else:
    print("You entered a wrong number. Please enter a valid number")



random_int = random.randrange(0, 2)

random_sign = "Any"

if random_int == 0:
    random_sign = rock
elif random_int == 1:
    random_sign = paper
else:
    random_sign = scissors



if sign == random_sign:
    print(f"You chose\n {sign})")
    print(f"The computer chose\n {random_sign}")
    print("There is a draw!")
elif (sign == rock) and (random_sign == scissors):
    print(f"You chose\n {sign})")
    print(f"The computer chose\n {random_sign}")
    print("You won!")
elif (sign == scissors) and (random_sign == paper):
    print(f"You chose\n {sign})")
    print(f"The computer chose\n {random_sign}")
    print("You won!")
elif (sign == paper) and (random_sign == rock):
    print(f"You chose\n {sign})")
    print(f"The computer chose\n {random_sign}")
    print("You won!")
else:
    print("You lose")
