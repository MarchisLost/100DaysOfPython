""" with open("Day25_csv_pandas/weather_data.csv") as data_file:
    data = data_file.readlines() """

""" import csv

with open('Day25_csv_pandas/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures) """

import pandas as pd

data = pd.read_csv('Day25_csv_pandas/weather_data.csv')
#print(data["temp"])

data_dic = data.to_dict()
#print(data_dic)

temp_list = data["temp"].to_list()
#print(temp_list)

#Calculate de mean
""" med = sum(temp_list) / len(temp_list)
print(med) """
# OR 
#print(data["temp"].mean())

#print(data.temp.max())

#Get data in rows
#print(data[data.day == 'Monday'])

#print(data[data.temp == data.temp.max()].condition)

# Create a dataframe from scratch
data_dict = {
    'Students': ['Amy', 'James',' Angela'],
    'Scores' : [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv('Day25_csv_pandas/new_data.csv')