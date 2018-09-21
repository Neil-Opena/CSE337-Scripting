#Commodities Trading
#Part 1
import time
price_file = open("prices_sample.csv")
date_dictionary = {} #day = key, value = time

for line in price_file:
    file_line = price_file.readline()
    line_list = file_line.split(",")
    epoch_date = line_list[0]
    formatted_date_time = (time.strftime("%Y-%m-%d %H:%M:%S",(time.gmtime(int(epoch_date))))).split(" ") #YYYY-MM-DD HH:MM:SS

    day = formatted_date_time[0]
    day_time = formatted_date_time[1]

    day_time_list = date_dictionary.get(day)
    if(day_time_list == None):
        date_dictionary[day] = [day_time]
    else:
        day_time_list.append(day_time)

price_file.close()

output_file = open("q1_p1_output.txt", "w")

for key in date_dictionary.keys():
    values = date_dictionary.get(key)
    output_file.write(key + ": ")
    output_file.write(",".join(values))
    output_file.write("\n")

output_file.close()
