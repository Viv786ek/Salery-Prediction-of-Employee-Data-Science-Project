#!/usr/bin/env python
# coding: utf-8

# In[5]:


# prog name : create df_from_excel.py
from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
#import mysql.connector as mysql
#from tkintertable import TableCanvas
from pandastable import Table

class create_df:
    def __init__(self,root):
        self.f=Frame(root,height=350, width=500)
        self.f.pack() # Place the frame on root window
    
        #Creating label widgets
        self.message_label = Label(self.f,text='Convert stock price Excel to Pandas DF ', font=('Arial', 14))
        
        #Buttons
        self.confirm_button= Button(self.f,text='convert', font=('Arial',14),bg='Orange',
                                   fg='Black', command=self.conv_to_df)
        self.exit_button=Button(self.f,text='Exit', font=('Arial',14),bg='Yellow',
                                fg='Black',command=root.destroy)
        
        #Placing the widgets using grid manager
        
        self.message_label.grid(row=1,column=0)
        self.confirm_button.grid(row=2,column=0)
        self.exit_button.grid(row=2,column=2)
        
    def conv_to_df(self):
        try:
            
            stock_price_df=pd.read_excel('stock_price.xls', sheet_name='Stock')
             #df.to_csv('stock_price.csv', index=False)
            if(len(stock_price_df)==0):
                msg.showinfo('No records in Excel File', ' No records in Excel file ')
            else:
                msg.showinfo('Pandas DF created ','Pandas DF created ')
            
            
            
            # Now display the DF in 'Table' object under 'pandastable' module
            self.f= Frame(root,height=200 , width=300)
            self.f.pack(fill=BOTH, expand=1)
            self.table= Table(self.f , dataframe=stock_price_df , read_only=True)
            self.table.show()
        except FileNotFoundError as e:
            msg.showerror('Excel file not found ','stock Price Excel file not found ')
            
#-------------------------------------------------------
root=Tk()
root.title('Conversion of stock Price Excel data to pandas DF')
root.geometry('800x600')
conv_csv= create_df(root)
root.mainloop()
        


# In[ ]:




