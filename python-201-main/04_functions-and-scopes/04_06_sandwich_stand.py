# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread_type, *toppings):
    sand_wich = ""
    sand_wich += f"Top bread slice of {bread_type} with "
    for top in toppings:
        sand_wich += f"{top}, "
    
    sand_wich += f"Bottoem bread slice of {bread_type}"
    return sand_wich

serve = make_sandwich("Wheat","Ham","eggs","Bacon")

print(serve)
