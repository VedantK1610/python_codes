import pandas as pd

df1=pd.read_csv('stock_data.csv')
print(df1)

print("\n")
#to replace unavaible data with NaN
df2=pd.read_csv('stock_data.csv',na_values={
    'eps':['not available',-1],
    'revenue':[-1],
    'price':['n.a.']
})
print(df2)
# df2.to_csv('new_stock.csv',index=False)  to create csv File

print("\n")
#methods to fill NaN data
# df2=df2.fillna(method='ffill')   #it will fill forward data with prev value
# df2=df2.fillna(0)    #fills NaN with 0

# df2=df2.interpolate()   #it will fill data by averaging

df2=df2.dropna()   #drops rows which have NaN value 
print(df2)