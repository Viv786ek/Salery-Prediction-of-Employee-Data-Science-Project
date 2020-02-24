from tkinter import *
from tkinter import messagebox as msg
import sys
import pandas as pd

import os.path
import csv
from pandastable import Table

class load_list_excel:
        def __init__ (self,root):
            self.f = Frame(root,height=350,width=500)
            self.f.pack()
            
            self.message_label = Label(self.f,text="Load/ Display Excel file of Stock Price, Int.Rate, Unemployment rate",font=("Arial",14))
            
            self.confirm_button = Button (self.f,text="Load & Display",font=('Arial',14),bg='Orange',fg='black',command=self.display_excel)
            self.exit_button = Button(self.f,text="Exit",font=('Arial',14),bg='yellow',fg='black',command=root.destroy)
            
            self.message_label.grid(row=1,column=0)
            self.confirm_button.grid(row=2,column=0)
            self.exit_button.grid(row=2,column=2)
            
        def display_excel(self):
            
            try:
                if(os.path.exists('D:\\Stockdata\\stock_price.xls')):
                    stock_price_df = pd.read_excel('D:\\Stockdata\\stock_price.xls')
                else:
                    msg.showerror('Excel file not found','stock price excel file not found')
                    
                if (len(stock_price_df)==0):
                    msg.showinfo('No records in Excel file','No records in excel file')
                    
                else:
                    msg.showinfo('Pandas DF created', 'Pandas DF created')
                    
                self.f = Frame(root, height=200, width=300)
                self.f.pack(fill=BOTH,expand=1)
                self.table = Table(self.f, dataframe= stock_price_df,read_only=True)
                self.table.show()
                
            except FileNotFoundError as e:
                    msg.showerror('excel file not found', 'stock price excel not found')
                    
                    


                    
                    
root=Tk()
root.title('Conversion Of Stock Index Price (Excel) Data To Pandas DF')
root.geometry('750x550')
list_excel = load_list_excel(root)
root.mainloop()
     
