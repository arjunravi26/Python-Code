# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)
# import pandas as pd
#
# data = pd.read_csv('weather_data.csv')
# print(data)
# print(type(data))
# data_dict = data.to_dict()
# # print(data['temp'])
# print(data_dict)
# data_list = data['temp'].to_list()
# avg = sum(data_list) / len(data_list)
# print(avg)
# avg = data['temp'].mean()
# print(avg)
# maximum = data['temp'].max()
# print(maximum)
# print(data.condition)
#
# Pandas working with row
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print(monday.temp)
# monday_fahrenheit = monday.temp[0] * 9 / 5 + 32
# print(monday_fahrenheit)
import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors = ['Gray', 'Red', 'Black']
# data_color = data[data['Primary Fur Color'].isin(colors)]
# print(data_color['Primary Fur Color'])
gray_color_count = len(data[data['Primary Fur Color'] == "Gray"])
cinnamon_color_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_color_count = len(data[data['Primary Fur Color'] == "Black"])
data_dict = {'Primary Fur Color': ['Gray', 'Cinnamon', 'Black'],
             'count': [gray_color_count, cinnamon_color_count, black_color_count]}
print(data_dict)
df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv', index=False)
