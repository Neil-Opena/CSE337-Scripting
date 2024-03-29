#Word Analytics
#Part 1

#get all of the file text, and separate by spaces
#for windows of n, put into dictionary, key = n-gram, value = count?

def get_n_gram_dictionary(file_name, n):

    dictionary = {}

    f = open(file_name, encoding="utf8")
    f_word_list = []
    for line in f:
        temp_list = (line.strip()).split(" ")
        f_word_list.extend(temp_list)
    
    #f_contents = f.read().strip()
    #f_word_list = f_contents.split(" ")

    for i in range(0, len(f_word_list) - (n - 1)):
        n_gram = " ".join(f_word_list[i:n + i])
        num_occurrences = dictionary.get(n_gram)
        if(num_occurrences == None):
            dictionary[n_gram] = 1
        else:
            num_occurrences += 1
            dictionary[n_gram] = num_occurrences

    # final result is dictionary containing n-grams with more than 1 occurrence
    for key in list(dictionary.keys()):
        if(dictionary[key] == 1):
            dictionary.pop(key)

    f.close()


    return dictionary

