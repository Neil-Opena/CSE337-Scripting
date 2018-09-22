#Commodities Trading
# Part 2
import math
price_file = open("q1_p1_output.txt")

total_tuple_list = []

def create_date_price_tuple(date, price):
    return (date, int(price))

def get_furthest_prices_dictionary(tuple_list, index, stride):
    dictionary = {}
    while True:
        day = tuple_list[index][0]
        price = tuple_list[index][1]
        if not (day in dictionary):
            dictionary[day] = price
        if(len(dictionary) >= 5):
            break
        index+=stride
    return dictionary

def calculate_ith_percentile(sorted_list, ith_percentile):
    # if n*p an integer, calculate (x_(k) + x(k+1)) / 2
    index = int(len(sorted_list) * ith_percentile)

    return (sorted_list[index] + sorted_list[index + 1])/2


for date_string in price_file:
    temp_str = date_string.split(":")

    str_price_list = (temp_str[1]).strip().split(",")
    date = temp_str[0]

    temp_list = ([create_date_price_tuple(date, x) for x in str_price_list])

    total_tuple_list.extend(temp_list)

list.sort(total_tuple_list, key=lambda my_tuple : my_tuple[1])

prices_list = list(map(lambda my_tuple : my_tuple[1], total_tuple_list))
sum_prices = sum(prices_list)
num_prices = len(prices_list)
mean = sum_prices / num_prices

percentile_25th = calculate_ith_percentile(prices_list, .25)
percentile_50th = calculate_ith_percentile(prices_list, .50)
percentile_75th = calculate_ith_percentile(prices_list, .75)

summation_mean_difference = sum([(x - mean)**2 for x in prices_list])
variance = summation_mean_difference / num_prices

print("25th percentile:", percentile_25th)
print("50th-percentile:", percentile_50th)
print("75th-percentile:", percentile_75th)
print("Variance:", variance)


dates_furthest_prices = get_furthest_prices_dictionary(total_tuple_list, 0, 1) # get prices that are significantly less than mean
dates_furthest_prices.update(get_furthest_prices_dictionary(total_tuple_list, -1, -1)) # get prices that are significantly greater than mean

mean_difference_list = []
for date in dates_furthest_prices.keys():
    price = dates_furthest_prices[date]
    mean_difference = math.fabs(price - mean)
    mean_difference_list.append((date, mean_difference))
list.sort(mean_difference_list, key=lambda date_price_tuple: date_price_tuple[1])

print("Days farthest from mean price (", mean, "): ")
for index in range(-1, -6, -1):
    date = mean_difference_list[index][0]
    print("\t",date, dates_furthest_prices[date])
price_file.close()
