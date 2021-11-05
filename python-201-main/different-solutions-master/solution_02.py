'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

value_list = []
# loop through unsorted list to append index 1 of tuole to value_list
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

print(value_list)
value_list.sort() # sort value_list 

# loop through value_list toc compare value with unsorted_list to push through to sorted_list
for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
            break

print(sorted_list)
