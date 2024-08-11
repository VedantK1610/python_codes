import  pandas as pd

df=pd.read_csv('weather_by_cities.csv')
print(df)

#group by
print("\n")
g=df.groupby('city')
# for city,city_df in g:
#     print(city)
#     print(city_df)

#to get perticular city df
# print(g.get_group('mumbai'))

#to get maximum value of each city
print(g.max())