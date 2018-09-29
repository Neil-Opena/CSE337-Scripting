#Coding For Fun
#Part 2
def modify_list(exponent_list):
    exponentiated_values = list(map(lambda exp: 2**exp, exponent_list))
    modified_list = list(filter(lambda value: value < 1000, exponentiated_values))
    return modified_list
my_list = [1, 4, 20]
print(modify_list(my_list))