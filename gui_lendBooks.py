import tkinter as tk
from tkinter import ttk as ttk, messagebox
import db_conn
from mysql.connector import Error
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import ttkthemes 
from gui_HoverButton import HoverButton
from PIL import Image, ImageTk
from datetime import datetime
from datetime import timedelta


class LendBooks(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        ttk.Label(self,background="#1f1f1f").pack(expand= True, fill="both")
        
        self.place(x=256, y=0, relwidth=0.8, relheight=1)
      
        self.top_main_frame = tk.Frame(self, background="#1f1f1f" ,autostyle=False)
        self.top_main_frame.place(x=0, y=0, relwidth=1, relheight=0.4)
        
        self.topbg = tk.Label(self, bg="#141414", height=3, width=250, autostyle=False)
        self.topbg.place(x=0, y=0)
        
        # self.logo_import = Image.open("img/lend.png").resize((256,256))                     
        # self.logo_tk = ImageTk.PhotoImage(self.logo_import)
        
        # self.lend_logo = ttk.Label(self, image=self.logo_tk, background="#1f1f1f")   
        # self.lend_logo.place(relx=0.15, rely=0.08)
        
        self.create_books_table()
        self.create_lend_table()
        self.create_menu()
    
    def create_menu(self):
        
        self.lend_book_btn1 = HoverButton(self, text="Ausleihen", command=self.insert_lend_data, bg="#141414",
                                        font=("Verdana" ,"15", "underline"), activebackground="#141414", 
                                        activeforeground="#df4807")
        self.lend_book_btn1.place(relx=0.03, rely=0.02)
        
    def create_lend_table(self):
        
        # Daten für die Spalten
        self.coldata = [
             {"text": "Leihnummer", "stretch": False, "width":125},
             {"text": "Titel", "stretch": False, "width":185},
             {"text": "geliehen von", "stretch": False, "width":200},
             {"text": "geliehen am", "stretch": False, "width":200},
             {"text": "Rückgabedatum", "stretch": False, "width":200}
            
             ]

        self.rowdata = self.get_lend_data()
        
        # Tabelle definieren
        self.lend_table = Tableview(
            master=self.top_main_frame,
            coldata=self.coldata,
            rowdata=self.rowdata,
            paginated=True,
            searchable=True,
            bootstyle=DARK,
            height=5,
            stripecolor=("#212121", "#ffffff"),
            pagesize=5,
        )
        # Tabelle plazieren
        self.lend_table.place(relx=0.01, rely=0.25)
        
        # Style für die Tabelle
        style = ttk.Style(self)                                                                                    
        ttkthemes.themed_style.ThemedStyle(theme="black")                                                           
        style.theme_use("black")                                                                                    
        style.configure("Treeview", background="#191717", fieldbackground="#191717", foreground="white", font="Verdana 10", rowheight=25)            
        style.configure('Treeview.Heading', background="#212121", foreground="white", borderwidth=0, font="Verdana 11 bold")   
        style.map('Treeview', background=[('selected', '#df4807')], foreground=[("selected", "white")])      
    
    def create_books_table(self):
        
         # Daten für die Spalten
        self.coldata = [
             
             {"text": "Titel", "stretch": False, "width":200},
             {"text": "Autor", "stretch": False, "width":180},
             {"text": "Verlag", "stretch": False, "width":180},
             {"text": "Kategorie", "stretch": False, "width":150},
             {"text": "ISBN", "stretch": False, "width":120},
             {"text": "Verfügbar", "stretch": True, "width":100},
             ]

        self.rowdata = self.get_book_data()
        
        # Tabelle definieren
        self.books_table = Tableview(
            master=self,
            coldata=self.coldata,
            rowdata=self.rowdata,
            paginated=True,
            searchable=True,
            bootstyle=DARK,
            height=12,
            stripecolor=("#212121", "#ffffff"),
            pagesize=12,
        )
        # Tabelle plazieren
        self.books_table.place(relx=0.01, rely=0.45)
        
        
        # Style für die Tabelle
        style = ttk.Style(self)                                                                                    
        ttkthemes.themed_style.ThemedStyle(theme="black")                                                           
        style.theme_use("black")                                                                                    
        style.configure("Treeview", background="#191717", fieldbackground="#191717", foreground="white", font="Verdana 10", rowheight=25)            
        style.configure('Treeview.Heading', background="#212121", foreground="white", borderwidth=0, font="Verdana 11 bold")   
        style.map('Treeview', background=[('selected', '#df4807')], foreground=[("selected", "white")])        

        
        
    def get_book_data(self):

            try:
                con = db_conn.conn
                cur = con.cursor()

                cur.execute("SELECT title, author, publisher, category, isbn, stock FROM books")
                self.rowdata = cur.fetchall()
               
                return self.rowdata
                
            except:
                messagebox.showerror("Fehler" , "Fehler bei der Datenbankverbindung!")
                
                
    def get_lend_data(self):

            try:
                con = db_conn.conn
                cur = con.cursor()

                cur.execute("SELECT lend_id, book_title, user_lastname, lenddate, returndate FROM lend_books")
                self.rowdata = cur.fetchall()
               
                return self.rowdata
                
            except:
                messagebox.showerror("Fehler" , "Fehler bei der Datenbankverbindung!")

    def insert_lend_data(self):
        
        self.get_date()
        self.lenddate = self.today
        
        # +14 Tage
        self.returndate = self.lenddate + timedelta(days = 14)
        print(self.returndate)
        
        self.get_row_data()
        self.rowdata = self.row
        
        
        print(self.rowdata)
        print(self.rowdata[0].values[0])
        
        try:
            self.conn = db_conn.conn
            self.myCursor = self.conn.cursor()
            self.myCursor.execute("Insert into lend_books(book_title,lenddate,returndate) values (%s,%s,%s)",[self.rowdata[0].values[0],self.lenddate,self.returndate])
            self.conn.commit() # Daten aus den Textfeldern entgegennehmen ([b.get(),c.get(),g]) und in die Datenbak schreiben

            self.create_lend_table()
            #messagebox.showinfo('Erfolg', "{} wurde hinzugefügt!".format(self.name.get())) #Infofenster bei Erfolg
          
              
        except Error:
            messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbinduung mmit der DB fehl, Error Message

    def get_row_data(self):
        
        self.row = self.books_table.get_rows(selected=True)
        
        print(self.row[0].values[0])
        return self.row    
    
    def get_date(self):
        
        self.today = datetime.now()
        print(self.today)
        return self.today