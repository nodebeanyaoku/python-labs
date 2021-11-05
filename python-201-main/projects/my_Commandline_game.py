import pathlib
import time
import random


inventory = ['fists']
game = True


def game_option(choice):
    
    if choice == 'option':
        print("type in [inv] inventory, [quit] to quit game\n")
        choice = input()

        if choice == 'inv':
            for i in inventory:
                print(i)
        

def door_left(choice):
    if choice == "left":
        print('You enter the left door...')
        time.sleep(1)
        print('You found a sword! ')
        inventory.append('sword')
        choice = input('Would you like to explore the other door or exit the center room? ')
        if choice == 'explore':
            print('You open the right door in the center room...')
            time.sleep(1.5)
            choice = input('Oh no, there\'s a temple guard! Do you fight or flee? ')
            
print("Welcome to the Midgard Dragonslayer!!!!\nEnter your name to begin: ")
name = input()
print(f'\n\nHello {name} welcome to the world of Dragons. If at any point you get stuck, type "quit" to quit game.')

time.sleep(3)

while game:

    print("There's been stories about a dragon in an abandoned castle \n You've decided to go on a quest to slay the dragon\n type [option] to see game options or type [quest] to leave for Quest\n ")
    play = input()
    game_option(play)
    time.sleep(3)

    
    if play == 'quest':
        print(f"{name} leaves the village on an adventure to dragon castle.\n you enter castles gates and is faced with two doors.\n choose left or righ door  ")
        choice = input()

        if choice == "left":


        if choice == "right":


        if choice == "quit":
            quit()