import pandas as pd

df =pd.read_csv('temperature.csv')
# print(df)
# print(df.shape) #gives rows and columns
# print(df.head(6)) #gives first 6 rows
# print(df[2:5])    #gives row 2 to 4
print(df.columns)  #gives names of columns
# print(df.month.head(5))  #gives data from column named month
# print(df[['City','Country']].head(5)) #only prints data of column city and country

#operations
# print(df['AverageTemperatureUncertaintyFahr'].max())  #gives max temprature
# print(df[['AverageTemperatureFahr','AverageTemperatureUncertaintyFahr']].describe()) #gives all info about this columns

#conditions
# print(df[df.AverageTemperatureFahr==df.AverageTemperatureFahr.max()]) #gives whole row which satisfy condition
print(df[['City','Country','AverageTemperatureFahr','month','year']][df.AverageTemperatureFahr==df.AverageTemperatureFahr.max()])
#above line will print the metioned colums only which satisfies condition

#set_index
# df.set_index('City',inplace=True) #now city is my index of table
# print(df.loc['Tottori'])  #gives all data relevant to city name tottori
# df.reset_index(inplace=True)  #to reset index again to 0,1,2...
# print(df)  


