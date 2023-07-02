import os
import random
from art import logo, vs
from data import data


def higher_lower():

    def details(celebrity, letter):
        """Gets the name, country and description of the selected entities"""
        story =""
        for _ in celebrity:
            name = celebrity["name"]
            description = celebrity["description"]
            country = celebrity["country"]
        story = f"Compare {letter}: {name}, a {description} from {country}"
        return story

    def winning_entity(celebrity_a, celebrity_b):
        """This function returns the winner between the selected persons """
        if celebrity_a['follower_count'] > celebrity_b['follower_count']:
            return celebrity_a
        else:
            return celebrity_b

    def followers(celebrity):
        """To get the number of instagram followers"""
        for _  in celebrity:
            follow = celebrity["follower_count"]
        return follow

    score = 0
    end_game = False

    entity_a = random.choice(data)

    os.system('cls')
    print(logo)

    while end_game != True:

        entity_b = random.choice(data)
        entity_c = random.choice(data)

        if entity_b == entity_a:
            entity_b = entity_c

        compare = ["A", "B"]
        line_A = details(entity_a, compare[0])
        line_B = details(entity_b, compare[1])

        following_a = followers(entity_a)
        following_b = followers(entity_b)

        if following_a > following_b:
            winner = "A"
        else:
            winner = "B"

        print(line_A)

        print(vs)

        print(line_B)

        question = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        if winner == question:
            score += 1 
            entity_a = winning_entity(entity_a, entity_b)
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