# Delimiters field is used to denote the characters to be used
# as delimiters(In addition to spaces).
import re

def get_words(text, delimiters):
    s = {'.', '^', '$', '*', '+', '?', '{', '}', '[', ']', '\\', '|', '(', ')'}
    list_d = list(delimiters)
    list_r = list()
    for d in list_d:
        if(d in s):
            list_r.append('\\' + d)
        else:
            list_r.append(d)
    list_r.append('\s') # include whitespace
    r = '|'.join(list_r)
    words = re.split(r, text)
    filtered_words = list(filter(lambda x: x != '', words)) # get non empty words
    return filtered_words

''' Returns the number of words in the input, using a string of delimiters to specify where to split the words'''
def word_count(text, delimiters):
    words = get_words(text, delimiters)
    print('words:\t' + str(words) + '\nword count:\t' + str(len(words))) # for testing purposes
    return len(words)

''' Returns the number of characters in the input'''
def character_count(text): 
    # no delimiter needed
    return len(text)

''' Returns the most frequent five words in the input, 
using a string of delimiters to specify where to split the words'''
def frequent_five_words(text, delimiters):
    words = get_words(text, delimiters)
    frequency = dict()
    for word in words:
        if(frequency.get(word) == None):
            frequency[word] = 0
        frequency[word] += 1

    # sort by frequency
    sorted_words =list(reversed(sorted(frequency.items(), key = lambda x: x[1])))
    frequent_five = sorted_words[:5]
    return frequent_five