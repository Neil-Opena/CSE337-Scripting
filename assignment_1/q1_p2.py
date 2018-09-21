#Commodities Trading
# Part 2
import time
price_file = open("prices_sample.csv")

date_price_list = []
sum = 0
line_num = 0
line = price_file.readline()
while line:
    line_list = line.split(",")
    epoch_date = line_list[0].strip()
    price = int(line_list[1].strip())

    day = time.strftime("%Y-%m-%d",(time.gmtime(int(epoch_date)))) #YYYY-MM-DD HH:MM:SS
    date_price_list.append((day, price))

    sum+=price

    line_num += 1

    line = price_file.readline()

price_file.close()

list.sort(date_price_list, key=lambda day_price_tuple: day_price_tuple[1])

output_file = open("DELETE_q1_p2.txt", "w")

for day_price_tuple in date_price_list:
    output_file.write(str(day_price_tuple))
    output_file.write("\n")

output_file.close()

print(sum)
print(line_num)
