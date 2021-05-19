import pandas as pd

df = pd.read_csv('BreadBasket_DMS.csv')
best30 = df.groupby('Item').count().sort_values(by='Date',ascending=False)
print(best30[:10])