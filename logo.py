import itertools


# this aims to get the most occurent letters of a word and sort in the most ascending to descending open
word = str(input())
letter = word.split(sep='')
letteredWordlen = len(letter)

occurrence = 0
charOccurrenceDictionary = dict.fromkeys(letter, occurrence)


print(dict(sorted(charOccurrenceDictionary.items(), key=lambda item: item[1], reverse=True)))

# Create an iterator that returns the characters
# from index 1 to the end of the string
char_iter = itertools.islice(word, 0, None)

# # Iterate over the selected characters
# for char in char_iter:
#     print(char)
# my_string = "Hello, Python!"
# def print_upper(char):
#     print(char.upper())
# list(map(print_upper, my_string))
# while charOccurrenceDictionary.get(letter) == None:

