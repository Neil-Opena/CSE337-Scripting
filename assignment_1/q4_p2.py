#Word Analytics
#Part 2

from q4_p1 import get_n_gram_dictionary

n_gram_dictionary = get_n_gram_dictionary("q4_p2_gutenberg.txt", 3)

list_keys = list(n_gram_dictionary.keys())
list.sort(list_keys, key=lambda dict_key: len(dict_key))
#sort the list of keys by length

highest_total_length = list_keys[-10:]
print(highest_total_length)
