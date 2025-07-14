import pandas as pd
import extraction_data as ed
url="https://raw.githubusercontent.com/safiyanaaz155/Retail-ETL-project/refs/heads/main/retail_sales_dataset.csv"
df=pd.read_csv(url)
df['Gender']=df['Gender'].str.strip().str.title()
df['Product Category']=df['Product Category'].str.strip().str.title()

df.drop_duplicates(inplace=True)
df['Calculated Total']=df['Quantity'] * df['Price per Unit']
mismatches = df[df['Total Amount'] != df['Calculated Total']]
print(f"🔍 Mismatched rows: {len(mismatches)}")

df['Total Amount'] = df['Calculated Total']
df.drop('Calculated Total', axis=1, inplace=True)

def age_group(age):
    if age < 18:
        return 'Teen'
    elif age < 35:
        return 'Young Adult'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['Age Group'] = df['Age'].apply(age_group)

df.to_csv("cleaned_retail_data.csv", index=False, encoding='utf-8')
print(df.head())
print("Data cleaned and saved as 'cleaned_retail_data.csv'")