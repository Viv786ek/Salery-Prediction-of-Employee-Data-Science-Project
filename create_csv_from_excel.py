


# Prog name : create_csv.py

from tkinter import *
from tkinter import messagebox as msg
import sys
import pandas as pd
#import mysql.connector as mysql
import os.path
import csv
from pandastable import Table
from tkintertable import TableCanvas

class create_csv:
    
    def __init__(self,root):
        self.f= Frame(root, height=350, width=500)
        self.f.pack() # Place the frame on root window
        
        #Creating label widgets
        self.message_label = Label(self.f,text='Conversion of stock Price Excel file to CSV ' , font=('Arial', 14))
        
        #Buttons
        self.confirm_button= Button(self.f,text='Load & Display', font=('Arial',14),bg='Orange', fg='Black', command=self.display_excel)
        self.exit_button=Button(self.f,text='Exit', font=('Arial',14),bg='Yellow', fg='Black',command=root.destroy)
        
        #Placing the widgets using grid manager
        
        self.message_label.grid(row=1,column=0)
        self.confirm_button.grid(row=2,column=0)
        self.exit_button.grid(row=2,column=2)
        
    def display_excel(self):
        try:
            stock_price_df=pd.read_excel('E:\project5\stock_price.xls', sheet_name='Stock')
            stock_price_df.to_csv('E:\project5\stock_price.csv', index=False)
            
            # Now display the csv in 'tkintertable' widget
            self.f= Frame(root,height=200 , width=300)
            self.f.pack(fill=BOTH, expand=1)
            self.table= TableCanvas(self.f , read_only=True)
            self.table.importCSV('E:\project5\stock_price.csv')
            #print(self.table.mode1.columnNames)# to print column names in IDLE shell
        except FileNotFoundError as e:
            print(e)
            
            

            
#-------------------------------------------------------
root=Tk()
root.title('Conversion of stock Price Excel data to pandas DF')
root.geometry('800x600')
conv_csv= create_csv(root)
root.mainloop()


# In[ ]:





# In[ ]:




