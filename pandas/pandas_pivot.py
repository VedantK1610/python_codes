import pandas as pd

df=pd.read_csv('weather_by_cities.csv')
print(df)
print("\n")
print(df.pivot(index='day',columns='city'))