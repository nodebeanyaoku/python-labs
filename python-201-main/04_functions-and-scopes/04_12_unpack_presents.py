# How can you call the function defined below using the given
# dictionary as its input.
# You shouldn't explicitly access the dict values, but use
# dictionary unpacking when passing the argument instead.

def congratulate(**kwargs):
    for key, val in kwargs.items():
        if key == "name":
            val1 = f"{val}"
        
        if key == "age":
            val2 = f"{val}"
        
    return print(f"Today {val1} is {val2} years old.\nHappy Birthday!")

user = {"name": "Adelheid", "age": 22}

congratulate(**user)