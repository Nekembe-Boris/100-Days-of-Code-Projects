import os
import random
from art import logo, vs
from data import data


def higher_lower():


    def highest_followers(person_a, person_b):
        """To get the number of instagram followers and returns A or B to compare with the user guess"""
        if person_a > person_b:
            return "A"
        elif person_b > person_a:
            return "B"
    
    def winning_celeb (celeb_a, celeb_b):
        """This function returns the winner between the selected persons """
        if celeb_a["follower_count"] > celeb_b["follower_count"]:
            return celeb_a
        elif celeb_b["follower_count"] > celeb_a["follower_count"]:
            return celeb_b


    entity_a = random.choice(data)
    score = 0

    end_game = False

    os.system('cls')
    print(logo)

    while end_game != True:

        entity_b = random.choice(data)

        if entity_a == entity_b:
            entity_b = random.choice(data)

        follower_a = entity_a['follower_count']
        follower_b = entity_b['follower_count']

        print("COMPARE:")
        print(f"\nA: {entity_a['name']} a {entity_a['description']} from {entity_a['country']}")

        print(vs)

        print(f"B: {entity_b['name']} a {entity_b['description']} from {entity_b['country']}")

        guess = input("\nWho has more followers? Type 'A' or 'B': ").capitalize()

        real_winner = highest_followers(follower_a, follower_b)

        if guess == real_winner:
            score += 1 
            entity_a = winning_celeb(entity_a, entity_b)
            os.system('cls')
            print(logo)
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry that's wrong. Final score {score}")
            repeat = input("Do you want to try again? Type 'y' or 'n': ")
            if repeat == "y":
                higher_lower()
            else:
                end_game = True

higher_lower()