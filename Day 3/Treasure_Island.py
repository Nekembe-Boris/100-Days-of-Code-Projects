from art import logo

print(logo)
print("Welcome to Treasure Hunt!!.")
print("Your mission is to find the treasure.")

junction = input("You're at a confluence which direction do you want to take? Right or Left? \n").lower()

if junction == "left":
    step1 = input("Do you want to Wait for the yatch or swim ? \n").lower()
    if step1 == "wait":
        step2 = input("You arrived at the Island unharmed. There is a house with 3 doors. Which door do you want to open? Red, Blue or Yellow? \n").lower()
        if step2 == "yellow":
            print("You found the treasure! You Win!")
        elif step2 == "blue":
            print("You entered a room of beasts. GAME OVER")
        elif step2 == "red":
            print("You chose a door that doesn't exist. GAME OVER")
        else:
            print("You fell into a hole. GAME OVER")
    else:
        print("Ops!! When you chill with the sharks, You know what comes next. GAME OVER")
else:
    print("Boom, You're lost at sea. GAME OVER")
    