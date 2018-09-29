#Daily Data
import datetime
date_price_file = open("q1_p1_output.txt")

weekly_prices = {}

for day_price_line in date_price_file:
    temp_str = day_price_line.split(":")
    day = temp_str[0]
    prices = [int(price) for price in temp_str[1].strip().split(",")]
    formatted_time = datetime.datetime.strptime(day, "%Y-%m-%d")

    day_of_week = formatted_time.weekday()
    if(day_of_week == 0):
        #the day corresponds to the beginning of the week
        weekly_prices[formatted_time] = prices
    else:
        #keep subtracting days until a key is found
        start_of_week = formatted_time - datetime.timedelta(days = day_of_week)
        if(start_of_week not in weekly_prices.keys()):
            weekly_prices[start_of_week] = prices
        else:
            weekly_prices[start_of_week].extend(prices)

output_file = open("q2_output.txt", "w")
for key in weekly_prices.keys():
    prices  = weekly_prices[key]
    list.sort(prices)
    date_string = key.strftime("%Y-%m-%d")

    max_price = prices[-1]
    min_price = prices[0]
    weekly_price = 0
    for price in prices:
        weekly_price += price
    mean_price = weekly_price / len(prices)

    output_file.write(date_string + ", ")
    output_file.write(str(max_price) + ", ")
    output_file.write(str(min_price) + ", ")
    output_file.write(str(mean_price))
    output_file.write("\n")
    
output_file.close()

