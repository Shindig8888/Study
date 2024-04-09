import pandas

squarrer_data = pandas.read_csv(r"C:\Users\claix\OneDrive\Desktop\codes\Study\Python\udemy\python100\day25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_squarrer = squarrer_data['Primary Fur Color'].to_list()

print(squarrer_data['Primary Fur Color'].unique())

count_grey_squarrer = color_squarrer.count('Gray')
count_cinnamon_squarrer = color_squarrer.count('Cinnamon')
count_black_squarrer = color_squarrer.count('Black')

squarrer_color_dict = {
    'Color': ['grey', 'cinnamon', 'black'],
    'Count' : [count_grey_squarrer, count_cinnamon_squarrer, count_black_squarrer]
}

count_data = pandas.DataFrame(squarrer_color_dict)
count_data.to_csv('squirrel_count.csv')