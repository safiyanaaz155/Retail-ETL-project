import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('cleaned_retail_data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')


# Plotting the total sales per day using line chart
sales=df.groupby('Date')['Total Amount'].sum()
plt.figure(figsize=(12, 6))
sales.plot(kind='line',color='blue', marker='o')
plt.title('Total sales per day')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.tight_layout()


#Plotting the total sales per Product Category using bar chart
category_sales = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
category_sales.plot(kind="bar",color='blue')
plt.title('Total sales per Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.tight_layout()

#proportion of sales by Product Category
plt.figure(figsize=(8, 8))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Sales by Product Category")
plt.axis('equal')

plt.show()
