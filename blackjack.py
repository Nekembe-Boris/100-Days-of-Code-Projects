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