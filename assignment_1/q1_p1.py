#Commodities Trading
#Part 1
import time
price_file = open("prices_sample.csv")
my_dictionary = {} #day = key, value = time

for file_line in price_file:
    line_list = file_line.split(",")
    epoch_date = line_list[0].strip()
    price = line_list[1].strip()

    formatted_date_time = (time.strftime("%Y-%m-%d %H:%M:%S",(time.gmtime(int(epoch_date))))).split(" ") #YYYY-MM-DD HH:MM:SS
    day = formatted_date_time[0]

    prices_list = my_dictionary.get(day)
    if(prices_list == None):
        my_dictionary[day] = [price]
    else:
        prices_list.append(price)

price_file.close()

output_file = open("q1_p1_output.txt", "w")

for key in my_dictionary.keys():
    values = my_dictionary.get(key)
    output_file.write(key + ": ")
    output_file.write(",".join(values))
    output_file.write("\n")

output_file.close()
