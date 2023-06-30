import os
import random


def higher_lower():

    def details(celebrity, letter):
        story =""
        for _ in celebrity:
            name = celebrity["name"]
            description = celebrity["description"]
            country = celebrity["country"]
        story = f"Compare {letter}: {name}, a {description} from {country}"
        return story

    def winning_entity(celebrity_a, celebrity_b):
        if celebrity_a['follower_count'] > celebrity_b['follower_count']:
            return celebrity_a
        else:
            return celebrity_b

    def followers(celebrity):
        for _  in celebrity:
            follow = celebrity["follower_count"]
        return follow

    score = 0
    end_game = False

    entity_a = random.choice(data)

    while end_game != True:

        os.system('cls')

        entity_b = random. choice(data)

        compare = ["A", "B"]
        line_A = details(entity_a, compare[0])
        line_B = details(entity_b, compare[1])

        following_a = followers(entity_a)
        following_b = followers(entity_b)

        #to delete
        print(following_a)
        print(following_b)

        if following_a > following_b:
            winner = "A"
        else:
            winner = "B"

        print(winner)

        print(line_A)

        print(line_B)

        question = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        if winner == question:
            score += 1 
            entity_a = winning_entity(entity_a, entity_b)
        else:
            print("Lose")
            end_game = True

higher_lower()