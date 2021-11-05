# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.
 
newList = randlist

 
 
# objective 1:
newList.sort()
 
# step 1: establish whether the list can be divided into tuples of two
# example: [1, 2, 3, 4] -> [(1, 2), (3, 4)] correct
# counterexample: [1, 2, 3] -> [(1, 2), (3, ????)] incorrect
 
if len(newList) % 2 != 0:
    newList.append(0)
 
# step 2: go through the list and start pairing the elements
list_of_tuples = []
for i in range(0, len(newList), 2):
    list_of_tuples.append( (newList[i], newList[i+1]) )
 
print(list_of_tuples)