#Coding for Fun
#Part 1
for num in range(100, 1000):
    string_num = str(num)
    sum_values = 0
    for place in string_num:
        value = lambda x: int(x)**3
        sum_values += value(place)
    if(sum_values == num):
        print(num)