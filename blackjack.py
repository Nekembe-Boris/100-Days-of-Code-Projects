import random
import os


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