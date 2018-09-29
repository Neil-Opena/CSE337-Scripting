#Coding for Fun
#Part 3
def count_words(words_list):
    dictionary = {}
    for word in words_list:
        count = len(list(filter(lambda test_word: word == test_word, words_list)))
        dictionary[word] = count

    return (list(map(lambda key: (key, dictionary[key]), dictionary.keys())))

my_list = ['dog','cat','dog','monkey', 'squirrel', 'monkey','cat']
print(count_words(my_list))