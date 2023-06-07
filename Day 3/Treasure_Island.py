print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

junction = input("You're at a confluence which direction do you want to take? Right or Left? \n")
lower_junction = junction.lower()

if lower_junction == "left":
    step1 = input("Do you want to Wait for the yatch or Swim ? \n")
    lower_step1 = step1.lower()
    if lower_step1 == "wait":
        step2 = input("You are now at the Island. Which door do you want to open? Red, Blue or Yellow \n")
        lower_step2 = step2.lower()
        if lower_step2 == "yellow":
            print("You found the treasure! You Win!")
        elif lower_step2 == "blue":
            print("You enter a room of beasts. GAME OVER")
        elif lower_step2 == "red":
            print("You chose a door that doesn't exist. GAME OVER")
        else:
            print("You fell into a hole. GAME OVER")
    else:
        print("Ops!! When you chill with the sharks, You know what comes next. GAME OVER")
else:
    print("Boom, You're lost at sea. GAME OVER")