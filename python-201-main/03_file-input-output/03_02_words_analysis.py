# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

# This is what the inside of the file would yield:
words_list = ['abc', 'aaa', 'aasd', 'dasqw', 'asdasdas', 'aaa', 'aa', 'bb', 'cc', 'qwer', 'eryyuy', 'qhwuiheuiq']
 
words_min = []
#initialize our length variable with something large so that we know our words are going to be shorter:
shortest_word_length = 9999999999999
 
words_max = []
#initialize our length variable with something small so that we know our words are going to be longer:
longest_word_length = 0
 
for w in words_list:
    # check if w is shorter than the shortest word so far - if yes, it's the new shortest word
    if len(w) < shortest_word_length:
        shortest_word_length = len(w)
        words_min = [w]
 
    # check if w is of equal length as the shortest word so far - if yes, it's a tie
    elif len(w) == shortest_word_length:
        words_min.append(w)
 
    # check if w is longer than the longest word so far - if yes, it's the new longest word
    if len(w) > longest_word_length:
        longest_word_length = len(w)
        words_max = [w]
 
    # check if w is of equal length as the longest word so far - is yes, it's a tie
    elif len(w) == longest_word_length:
        words_max.append(w)
 
print("Shortest words: ")
print(words_min)
 
print("Longest words: ")
print(words_max)