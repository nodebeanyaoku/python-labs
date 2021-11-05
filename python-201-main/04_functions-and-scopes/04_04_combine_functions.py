# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):  # Positional arguments in definition
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(name,text):
    letter = ""
    letter += greet("Hello",name) + f"\n"
    letter += f"{text}\n"
    letter += f"Goodbye {name}"
    return letter


message = write_letter("Nodebe","Today has been a great day")

print(message)