#Game initial setup
import time
game = True
sword = False

import requests

name_length = 0
# Check whether it meets the length requirements for the API call
while not (name_length >= 2 and name_length <= 40):
    # Collect the name from your player
    original_name = input("Enter your name: ")
    name_length = len(original_name)

# Ping the Uzby API to create a new random name for your player,
#   using the length of their given name as input
URL = f"https://uzby.com/api.php?min={name_length}&max={name_length}"
response = requests.get(URL)
name = response.text

# Inform the player about their in-game name
print(f"Welcome to the dungeon! In this world, your name won't be {original_name}.")
print(f"Instead, you'll be know as {name.upper()}!")

# Your game code follows here


#Game intro
name = input('\nEnter your name:\n')
time.sleep(2)
print(f'\nWelcome to the Game {name}\n')
time.sleep(2)
print('You will face a series of choices in this game. Choose wisely and you will become a WARRIOR. Thats the only way to leave this place.... alive')
time.sleep(1)
print('Good luck!!!')

#Game development
while game:
    time.sleep(2)
    doors = input('\nYou are in Room # 1 and have two doors in front of you (left or right)\nType which door you want to go through:\n')
    # INPUT VERIFIER doors
    while (doors != 'left') and (doors != 'right'):
        print('\nWhoops, that\'s not an option. Type only left or right')
        doors = input()
    
    if doors == 'left':
        
        while True:
            time.sleep(2)
            print('\nYou are in Room # 2, seemingly empty. You wanna look around?\nType yes or no (then you will return to Room # 1)')
            choice1 = input()
            # INPUT VERIFIER choice1
            while (choice1 != 'yes') and (choice1 != 'no'):
                print('\nWhoops, that\'s not an option. Type only yes or no')
                choice1 = input()

            if choice1 == 'no':
                break
            elif (choice1 == 'yes') and (sword == False):
                for i in range(0,5):
                        time.sleep(1)
                        print('.')
                print('\nWow!!! You found a sword. It looks so nice. Wanna grab it?\nType yes or no')
                choice2 = input()
                # INPUT VERIFIER choice2
                while (choice2 != 'yes') and (choice2 != 'no'):
                    print('\nWhoops, that\'s not an option. Type only yes or no')
                    choice2 = input()

                if choice2 == 'no':
                    print('\nThat\'s so sad :( Maybe you\'ll need it later on...')
                    continue    
                elif choice2 =='yes':
                    print(f'\nGreat! Now you have a sword. You are a WARRIOR {name}')
                    sword = True
                    continue
            elif (choice1 == 'yes') and (sword == True):
                for i in range(0,5):
                        time.sleep(1)
                        print('.')
                print('\nWell, there\'s nothing here anymore. Maybe you can try the right door in Room #1')
                continue

    elif doors == 'right':
        
        while True:
            time.sleep(3)
            print('\nYou encounter with a DRAGON. Wanna fight it? (TIP: Only do it if you are a WARRIOR)\nType yes or no')
            fight_dragon = input()
            # INPUT VERIFIER fight_dragon
            while (fight_dragon != 'yes') and (fight_dragon != 'no'):
                print('\nWhoops, that\'s not an option. Type only yes or no')
                fight_dragon = input()

            if fight_dragon == 'no':
                time.sleep(2)
                print('\nAlright, heading back')
                break
            elif fight_dragon == 'yes':
                time.sleep(2)
                print(f'\nThis is it {name}. Attack the Dragon!!!!\n')
                if sword == True:
                    time.sleep(2)
                    print('You are a WARRIOR and have your sword with you. Let\'s go!!!!')
                    for i in range(0,5):
                        time.sleep(1)
                        print('.')
                    print(f'You defeated the Dragon. You won {name}!!!\n')
                    game = False
                    break
                elif sword == False:
                    time.sleep(2)
                    print('You have no weapons with you, this is gonna be tough')
                    for i in range(0,5):
                        time.sleep(1)
                        print('.')
                    print(f'Sorry {name}, you were not a WARRIOR and the dragon ate you. You lose :(\n(TIP: Maybe you need to pick up a weapon next time)\n')
                    game = False
                    break