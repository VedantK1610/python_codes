import pandas as pd

it_df= pd.DataFrame({
    "staff":['L.M.R.J Lobo','M. Nirgude','S. Karpe'],
    "Labs":['DBMS lab','IT Lab','CN Lab'],
    "Income":[2000,4500,1000]
})

cse_df= pd.DataFrame({
    "staff":['Dixit','Patnaik','Gham'],
    "Labs":['CSE lab','SP lab','DP Lab'],
    "Income":[1500,6000,1200]
})

df=pd.concat([it_df,cse_df])
print(df)
print("\n")
df=pd.concat([it_df,cse_df],ignore_index=True)
print(df)
print("\n")
df=pd.concat([it_df,cse_df],keys=['IT','CSE'])
print(df.loc['IT'])

print("\n")
temp_df=pd.DataFrame({
    'city':['mumbai','pune','solapur'],
    'temprature':[25,30,35]
},index=[0,1,2])
wind_df=pd.DataFrame({
    'city':['pune','mumbai','solapur'],
    'windspeed':[21,22,12]
},index=[1,0,2])

df2=pd.concat([temp_df,wind_df],axis=1)
print(df2)
