"""
    Rock-Paper-Scissors Game
Code a game of rock paper scissors.

Instructions
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner
Some Tips
Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:
"""
import random

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    hand_choice = ["scissor", "rock", "paper"]
    for index in range(len(hand_choice)):
        if index == hand:
            return print(f"{hand_choice[index]}")

    # for example if the variable hand is 0, it should return the string "scissor"
    

def determine_winner(user1,user2):
    if user1 == 0 and user2 == 2:
        print(f"You won")
    if user1 == 2 and user2 == 1:
        print(f"You won")
    if user1 == user2: 
        print(f"its a draw")
    else:
        print(f"Computer won")


user_input = int(input("Enter in number: "))
computer_input = random.randint(0,2)


get_hand(user_input)
get_hand(computer_input)
determine_winner(user_input,computer_input)