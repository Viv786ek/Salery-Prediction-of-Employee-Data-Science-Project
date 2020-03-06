import pandas as pd
import matplotlib.pyplot as plt

stock_price_df=pd.read_excel('stock_price.xls')

plt.scatter(stock_price_df['Unemployment_Rate'], stock_price_df['Stock_Index_Price'], color='green')
plt.title('Stock Index Price Vs Unemployment Rate', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()
