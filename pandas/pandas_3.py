import pandas as pd
import numpy as np
import regex

df=pd.read_csv('weather_data.csv')
print(df)

print("\n")
#to replace value
df2=df.replace(-99999,np.NAN)   #we can also pass list to replace multiple values and also dic to change value column wise
# print(df2)

print("\n")
#regex => used to detect patterns and change value
df3=df.replace({
    'temperature':'[A-Za-z]',
    'windspeed':'[A-Za-z]',
},'',regex=True)
df3=df3.replace({
    'event':'0'
},'Sunny')
print(df3)
