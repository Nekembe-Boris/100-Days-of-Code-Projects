import random
from

random_word = random.choice(word_list)


#creating an empty list
display = []
for letter in range(0, len(random_word)):
    dash = "_"
    display.append(dash)

#forming a placeholder with the lenght of the random word
placeholder = ""
for n in range(0, len(display)):
    all_dash = display[n]
    placeholder = placeholder + all_dash

lives_left = 6
end_game = False

print(logo)
print("Welcome to HANGMAN!!")

print(f"\nWORD: {placeholder}")

while end_game != True:

    #getting user input and inserting it in a list if it matches any letter
    user_guess = input("\nGUESS A LETTER IN THE WORD:\n").lower()

    #checking if guessed letter has already been chosen else, including it in list
    if user_guess in display:
        print("You've already chosen this letter. Try again")
    else:
        for i in range(len(random_word)):
            if random_word[i] == user_guess:
                display[i] = user_guess

    #forming a placeholder for all the corret guesses and printing them out
    main_placeholder = ""
    for n in range(0, len(display)):
        all_dash = display[n]
        main_placeholder = main_placeholder + all_dash
    print(f"\nWORD: {main_placeholder}")

    #verifying if player guessed the wrong word and tracking lives left
    if user_guess not in random_word:
        lives_left -= 1
        print(f"You guessed letter {user_guess} and it's not in word")
        print(stages[lives_left])
    
    #ending game if player won or lost all lives
    if "_" not in display:
        end_game = True
        print("You Won!")
    elif lives_left == 0:
        end_game = True
        print("You Lost")       
