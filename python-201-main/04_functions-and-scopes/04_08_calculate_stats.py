# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(*args):
  # define the function here
 
  stat_list = []
  sentence = ""
  for a in args:
    stat_list.append(a)
  
  Sum = sum(stat_list)
  average = Sum / len(stat_list)
  max_value = max(stat_list)
  min_value = min(stat_list)
  sentence +=  f"Maximum number: {max_value} \nMinimum number: {min_value} \nThe Average: {average}\nSum of numbers: {Sum}"
  return sentence

  

# call the function below here

save = stats(*example_list)

print(save)