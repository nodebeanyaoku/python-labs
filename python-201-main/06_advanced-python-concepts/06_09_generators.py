# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.


nums = range(1, 1000000)
gen = (n for n in nums if n % 1111 == 0)

print(gen)