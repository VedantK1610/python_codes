import pandas as pd

temp_df=pd.DataFrame({
    'city':['mumbai','pune','solapur'],
    'temprature':[25,30,35]
})
wind_df=pd.DataFrame({
    'city':['pune','mumbai','solapur'],
    'windspeed':[21,22,12]
})
df=pd.merge(temp_df,wind_df,on='city')
print(df)