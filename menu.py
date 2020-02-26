# empsalmenu.py 
# Main menu program for Project 1

from tkinter import *
import sys
import os
import subprocess

class StockPrice:

    # Constructor
    def __init__(self, root):

        self.main_lbl=Label(root, text='Stock  Price  prediction  of  a  Fictious  Company \n by  using \n Interest Rate and Unemployment Rate', fg='dark blue', font=('Bernard MT Condensed', -30, 'underline'))
        self.main_lbl.place(x=200, y=250)
       
        # Create menubar
        self.menubar=Menu(root)
        root.config(menu=self.menubar)            # attach the menubar to root
        # Now create Single menubar operation menu
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Stock Price Excel/ Df file Maintenance', menu=self.mysql_menu)
        # Now create menu items under menubar 
        self.mysql_menu.add_command(label='List the Stock price Excel File', command=self.list_excel)
        self.mysql_menu.add_command(label='Build/List DF from Excel', command=self.create_df_from_excel)
        self.mysql_menu.add_command(label='Build/List the CSV from Excel', command=self.create_csv_from_excel)
         
        # Now add a separator
        self.mysql_menu.add_separator()
        # Now create a Exit menu
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        # Now create Data Maintenance operation menu
        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports on Pandas Df', menu=self.data_menu)
        self.data_menu.add_command(label='Find Intercept and Coefficient', command=self.Intercept)
        self.data_menu.add_command(label='Scatter Plot- Stock Price vs Interest', command=self.scatter)
        self.data_menu.add_command(label='Scatter Plot- Stock Price vs Unemployment', command=self.scatterunem)
        
        # Prediction Menu
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict Stock Price', command=self.Prediction)
         

    def list_excel(self):
        #subprocess.check_call(["python.exe","list_excel.py"])
        os.system("python E:\project5\list_excel.py")
    def create_df_from_excel(self):
        #subprocess.check_call(["python.exe","create_df_from_excel.py"])
        os.system("python E:\project5\create_df_from_excel.py")
    def create_csv_from_excel(self):
        #subprocess.check_call(["python.exe", "create_csv_from_excel.py"])
        os.system("python E:\project5\create_csv_from_excel.py")
    
    def Intercept(self):
        #subprocess.check_call(["python.exe", "Intercept.py"])
        os.system("python E:\project5\Intercept.py")
    def scatter(self):    
        #subprocess.check_call(["python.exe", "scatter.py"])
        os.system("python E:\project5\scatter.py")
    def scatterunem(self):
        #subprocess.check_call(["python.exe", "scatterunem.py"]) 
        os.system("python E:\project5\scatterunem.py")              

    def Prediction(self):
        #subprocess.check_call(["pythonw.exe", "Prediction.py"])  
        os.system("python E:\project5\Prediction.py")              

  
root=Tk()
root.title('Stock Price Prediction')

obj=StockPrice(root)
root.geometry('800x600')
root.mainloop()

                                 
        
        
        
        
                 
