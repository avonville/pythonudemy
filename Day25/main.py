import pandas

# data = pandas.read_csv('weather_data.csv')

# # data_dict = data.to_dict()

# # avg_temp = data['temp'].mean()

# # print( data[data.condition == 'Rain'] )

# # monday = data[data.day == 'Monday']
# # print( monday.condition )


# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)

# print( data )

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_color = data['Primary Fur Color']

gray = data['Primary Fur Color'].str.contains('Gray').sum()
cinnamon = data['Primary Fur Color'].str.contains('Cinnamon').sum()
black = data['Primary Fur Color'].str.contains('Black').sum()

fur_count_dict = {
    'Fur COlor': ['Gray', 'Cinnamon', 'Black'],
    'Count':[ gray, cinnamon, black]
}

fur_count_data = pandas.DataFrame(fur_count_dict)

print(fur_count_data)


# gray = data[ data['Primary Fur Color'] == 'Gray' ].count( axis='Primary Fur Color')

# count_gray = gray['Primary Fur Color'].count

# print( fur_color )
