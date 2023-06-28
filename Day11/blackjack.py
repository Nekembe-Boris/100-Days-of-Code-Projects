import random
import os
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ace = 11


def deal_card():
    for i in range(len(cards)):
        u_serve = random.sample(cards, 2)
        c_serve = random.sample(cards, 2)
    return u_serve, c_serve


user_cards, computer_cards = deal_card()

blackjack = [ace, 10]


def game():
    os.system('cls')
    print(logo)

    player_score = sum(user_cards)
    cpu_score = sum(computer_cards)

    def blackjack_check():
        if player_score == sum(blackjack) and cpu_score != sum(blackjack):
            print("You won")
            return 0
        elif cpu_score == sum(blackjack) and player_score != blackjack:
            print("You lose")
            return 0
        elif player_score == sum(blackjack) and cpu_score == sum(blackjack):
            return "It's a draw"

    push = blackjack_check()

    print(f"    Your hand: {user_cards}, current score {sum(user_cards)}")
    print(f"    Dealer's first card: [{computer_cards[0]}]")

    player_draw = False

    while player_score < 21 and player_draw != True:
        ask = input("Type 'y' to get another card, or type 'n' to pass: ")
        if ask == "y":
            user_cards.append(random.choice(cards))
            player_score = sum(user_cards)
            print(f"    Your hand: {user_cards}, current score {player_score}")
            print(f"    Dealer's first card: [{computer_cards[0]}]")
            if player_score > 21:
                print(f"    Your hand: {user_cards}, final score {sum(user_cards)}")
                print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
                print("You Lose. You went over")
                player_draw = True
            if cpu_score < 17:
                computer_cards.append(random.choice(cards))
                cpu_score = sum(computer_cards)
            
        elif ask == "n":
            if cpu_score < 17:
                computer_cards.append(random.choice(cards))
                cpu_score = sum(computer_cards)

                if cpu_score > 21:
                    print(f"    Your hand: {user_cards}, final score {sum(user_cards)}")
                    print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
                    print("You won, Computer went over!")
                    player_draw = True
                if cpu_score < 21:
                    computer_cards.append(random.choice(cards))
                    cpu_score = sum(computer_cards)
            player_draw = True
    
    if player_score < 22 and cpu_score < 22:
        if player_score < cpu_score:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("You lose")
        elif player_score > cpu_score:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("You Win!!")
        elif push == "It's a draw":
            print("There is a draw")
        else:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("There is a draw")

        repeat = False
    

    while repeat != True:
        replay = input("Do you want to play blackjack again? Type 'y' or 'n': ")

        if replay == "y":
            os.system('cls')
            game()
        else:
            repeat = True
            print("Goodbye")


entry = input("Do you want to play blackjack? Type 'y' or 'n': ")

if entry == "y":
    game()
else:
    print("Goodbye!!")