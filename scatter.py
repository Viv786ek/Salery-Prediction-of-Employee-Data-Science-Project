import pandas as pd
import matplotlib.pyplot as plt

stock_price_df=pd.read_excel('stock_price.xls')

plt.scatter(stock_price_df['Interest_Rate'], stock_price_df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()
