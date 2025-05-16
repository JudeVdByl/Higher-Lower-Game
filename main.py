import random
import art
from game_data import data



def versus_game():
    random.shuffle(data)
    keep_playing = 'y'
    current_score = 0
    random_b = random.choice(data)

    print(art.logo)
    while keep_playing == 'y':
        random_a = random_b
        random_b = random.choice(data)
        while random_b == random_a:
            random_b = random.choice(data)


        print (f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}")
        print(art.vs + "\n")
        print(f"Compare B: {random_b['name']}, a {random_b['description']}, from {random_b['country']}")

        u_choice = input(f"\nWho has more followers? Type 'A' or 'B': ").lower()
        print('\n' * 20)
        print(art.logo)

        if (
            (u_choice == 'a' and (random_a['follower_count'] > random_b['follower_count'])) or
            (u_choice == 'b' and (random_b['follower_count'] > random_a['follower_count']))
        ):
            current_score += 1
            print(f"\nYou're right! Current score: {current_score}\n")

        else:
            print('\n' * 20)
            print(f"\nSorry that's wrong! Final score: {current_score}")
            print(art.logo)
            current_score = 0

            if input('\nWould you like to keep playing?').lower() == keep_playing:
                print(art.logo)
                random.shuffle(data)
                random_b = random.choice(data)

            else:
                keep_playing = 'n'


    else:
        print("\nThanks for playing!")




versus_game()
