# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(*args):  # add your arguments
      # add your code implementation
    enu = []
    for a in args:
        enu.append(a)

    for index in range(len(enu)):
        print(f"{index}: {enu[index]}")
    


courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']
footballers = ['Messi','Ronaldo','Mbappe']
my_enumerate(*courses)
my_enumerate(*footballers)
