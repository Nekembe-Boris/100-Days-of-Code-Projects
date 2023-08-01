import random
import os
from art import logo

def game():

    os.system('cls')

    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ace = 11

    def deal_card():
        for i in range(len(cards)):
            u_serve = random.sample(cards, 2)
            c_serve = random.sample(cards, 2)
        return u_serve, c_serve


    user_cards, computer_cards = deal_card()

    blackjack = [ace, 10]

    player_score = sum(user_cards)
    cpu_score = sum(computer_cards)

    def blackjack_check():
        """This function checks the presence of a blackjack and returns 0 if yes"""

        if player_score == sum(blackjack) and cpu_score != sum(blackjack):
            return 0
        elif cpu_score == sum(blackjack) and player_score != blackjack:
            return 0

    push = blackjack_check()

    print(f"    Your hand: {user_cards}, current score {sum(user_cards)}")
    print(f"    Dealer's first card: [{computer_cards[0]}]")

    player_draw = False

    while player_score < 21 and player_draw != True:
        ask = input("Type 'y' to get another card, or type 'n' to pass: ")
        if ask == "y":
            user_cards.append(random.choice(cards))
            player_score = sum(user_cards)
            if player_score > 21:
                player_draw = True
            if cpu_score < 17:
                computer_cards.append(random.choice(cards))
                cpu_score = sum(computer_cards)
            
        elif ask == "n":
            if cpu_score < 21:
                computer_cards.append(random.choice(cards))
                cpu_score = sum(computer_cards)

            player_draw = True
            
    
    def compare_score(player_score, cpu_score):
        """This function takes the sum of cards and based on the coditions given, if prints out he winner"""
        if player_score == cpu_score:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("It's a Draw")
        elif cpu_score == push:
            print("You Lose. Dealer has a blackjack")
            print("")
        elif player_score == push:
            print("You win. You got a Blackjack!!")
        elif player_score > 21:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("You Lose. You went over")
        elif cpu_score > 21:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("You Win. Dealer went over")
        elif player_score > cpu_score:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("You Win.")
        else:
            print(f"    Your hand: {user_cards}, final score {player_score}")
            print(f"    Dealer's cards: {computer_cards}, final score {cpu_score}")
            print("You Lose.")

    compare_score( player_score, cpu_score)


repeat = False
while repeat != True:
    replay = input("Do you want to play blackjack? Type 'y' or 'n': ")

    if replay == "y":
        game()
    else:
        repeat = True
        os.system('cls')
        print(logo)
        print("Goodbye")