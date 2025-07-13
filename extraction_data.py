import pandas as pd
url="https://raw.githubusercontent.com/safiyanaaz155/Retail-ETL-project/refs/heads/main/retail_sales_dataset.csv"
df=pd.read_csv(url)
# display the first 5 rows of the dataframe
print(df.head())

#print data info
print("\ndata info:")
print(df.info())