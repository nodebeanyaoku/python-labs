# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divisible_by_4_or_7(number):
    if number % 4 == 0  or number % 7 == 0:
        return True
    else:
        return False
def divisible_by_4_and_7(num):
    if num % 4 == 0  and num % 7 == 0:
        return True
    else:
        return False



user = int(input("Enter in a number between and 1,000,000,000: "))

num_4_or_7 = divisible_by_4_or_7(user)
num_4_and_7 = divisible_by_4_and_7(user)

print(f"Is {user} divisible by 4 or 7:{num_4_or_7}")
print(f"Is {user} divisible by 4 and 7:{num_4_and_7}")


    
