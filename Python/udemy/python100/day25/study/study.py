# with open('weather_data.csv', 'r') as data_origin:
#     data = data_origin.readlines()

# data = list(map(str.strip, data))
# print(data)

# import csv
# with open('weather_data.csv', 'r') as data_origin:
#     data = csv.reader(data_origin)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#     temperature = temperature[1:]
#     temperature = list(map(int, temperature))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data["temp"]))
# print(type(data))
# data.info()

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# temp_average = round(sum(temp_list) / len(temp_list), 2)
# print(temp_average)

# temp_mean = data['temp'].mean()
# print(temp_mean)

# print(data['temp'].max())

# data["condition"]
# data.condition

#data from row
# data[data.day == 'Monday']

# print(data.temp)

# data[data.temp == data.temp.max()]

# monday = data[data.day == 'Monday']
# print(float(monday.temp) * 1.8+32)

# create a dataframe
data_dicr = {
    "students" : ["any", 'James', 'Angela'],
    "scores" : [75,86,95]
}

data = pandas.DataFrame(data_dicr)
data.to_csv("new_data.csv")