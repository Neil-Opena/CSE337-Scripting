#Daily Data
import time
import datetime
date_price_file = open("q1_p1_output.txt")

weekly_prices = {}

for day_price_line in date_price_file:
    temp_str = day_price_line.split(":")
    day = temp_str[0]
    formatted_time = datetime.datetime.strptime(day, "%Y-%m-%d")
    # if(formatted_time.tm_wday == 0): # wday = week day, Monday = 0
    #     weekly_prices[day] = list(map(int, temp_str[1].strip().split(",")))
    #     #else
    #     # find the corresponding key that corresponds to the day of the week
    print(formatted_time)
    
