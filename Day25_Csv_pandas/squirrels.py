import pandas as pd

data = pd.read_csv('Day25_csv_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

furColor = data['Primary Fur Color']

GrayColorCount = 0
CinnamonColorCount = 0
BlackColorCount = 0

for i in furColor:
    if i == 'Gray':
        GrayColorCount += 1
    elif i == 'Cinnamon':
        CinnamonColorCount += 1
    elif i == 'Black':
        BlackColorCount += 1

#print(f'Gray: {GrayColorCount} \nCinnamon: {CinnamonColorCount} \nBlack: {BlackColorCount}')

# OR

GrayColorCount2 = len(data[data['Primary Fur Color'] == 'Gray'])
CinnamonColorCount2 = len(data[data['Primary Fur Color'] == 'Cinnamon'])
BlackColorCount2 = len(data[data['Primary Fur Color'] == 'Black'])

#print(f'Gray: {GrayColorCount2} \nCinnamon: {CinnamonColorCount2} \nBlack: {BlackColorCount2}')

furColorCounts = {
    'FurColor' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [GrayColorCount2, CinnamonColorCount2, BlackColorCount2]
}
data = pd.DataFrame(furColorCounts)
print(data)
data.to_csv('Day25_csv_pandas/new_squirrels_data.csv')