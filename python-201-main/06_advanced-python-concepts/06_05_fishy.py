# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = []

[fish_list.append(word) for word in fish_tuple if word.endswith("fish")]

print(fish_list)