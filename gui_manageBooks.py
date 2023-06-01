import tkinter as tk
from tkinter import ttk as ttk, messagebox
import db_conn
from mysql.connector import Error
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

from gui_HoverButton import HoverButton



class ManageBooks(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self,background="#191717").pack(expand= True, fill="both")
        self.place(x=256, y=0, relwidth=0.8, relheight=1)
        self.create_table()
        self.add_book_gui()
        
       
        menu_separator1 = ttk.Separator(self, orient='vertical')
        menu_separator1.place(relx=0.23, rely=0.02, relwidth=0.001, relheight=0.25)
        
        menu_separator2 = ttk.Separator(self, orient='vertical')
        menu_separator2.place(relx=0.57, rely=0.02, relwidth=0.001, relheight=0.25)      
        
            
        manage_books_btn1 = HoverButton(self, text="Buch hinzufügen", bg="#191717", fg="white", 
                                        font=("Verdana" ,"15", "underline"),activebackground="#232121", 
                                        borderwidth="0", activeforeground="#df4807",autostyle=False
                                        )
        manage_books_btn1.place(relx=0.03, rely=0.02)
    
    def add_book_gui(self):
        
        
        
        self.name = tk.StringVar() 
        self.author = tk.StringVar()
        self.publisher = tk.StringVar()
        self.category = tk.StringVar()
        self.isbn = tk.StringVar()
        self.stock = tk.StringVar()
        
        self.add_book_label = tk.Label(self, text='Buchname:',bg='#191717',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.25, rely=0.02)
        self.add_book_entry1 = tk.Entry(self, textvariable=self.name, width=30)
        self.add_book_entry1.place(relx=0.36, rely=0.02)
        
        tk.Label(self, text='Autor:',bg='#191717',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.25, rely=0.06)
        self.add_book_entry2 = tk.Entry(self, textvariable=self.author, width=30)
        self.add_book_entry2.place(relx=0.36, rely=0.06)
        
        tk.Label(self, text='Verlag:', bg='#191717', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.25, rely=0.10)
        self.add_book_entry3 = tk.Entry(self, textvariable=self.publisher, width=30)
        self.add_book_entry3.place(relx=0.36, rely=0.10)

        tk.Label(self, text='Kategorie:', bg='#191717', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.25, rely=0.14)
        self.add_book_entry4 = tk.Entry(self, textvariable=self.category, width=30)
        self.add_book_entry4.place(relx=0.36, rely=0.14)
        
        tk.Label(self, text='ISBN:', bg='#191717', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.25, rely=0.18)
        self.add_book_entry5 = tk.Entry(self, textvariable=self.isbn, width=30)
        self.add_book_entry5.place(relx=0.36, rely=0.18)

        tk.Label(self, text='Menge:', bg='#191717', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.25, rely=0.22)
        self.add_book_entry6 = tk.Entry(self, textvariable=self.stock, width=30)
        self.add_book_entry6.place(relx=0.36, rely=0.22)
        
        tk.Button(self, text='Hinzufügen', width=21, font=('Arial', 10),command=self.add_book).place(relx=0.365,rely=0.26)
        
    def clear_book_gui(self):
            
        self.add_book_entry1.delete(0,tk.END)
        self.add_book_entry2.delete(0,tk.END)
        self.add_book_entry3.delete(0,tk.END)
        self.add_book_entry4.delete(0,tk.END)
        self.add_book_entry5.delete(0,tk.END)
        self.add_book_entry6.delete(0,tk.END)
        
    def add_book(self):

        if len(self.name.get()) == 0 or len(self.author.get()) == 0 or len(self.publisher.get()) == 0 or len(self.category.get()) == 0 or len(self.isbn.get()) == 0 or len(self.stock.get()) == 0: # Ist eines der Eingabefelder leer?
            messagebox.showerror("Fehler","Bitte füllen Sie alle Felder aus!")
        else:
            ava = 'TRUE' # Verfügbarkeit des Buchs, wenn ein Buch neu eingepflegt wird, ist es auch logischerweise verfügbar
            try:
                self.conn = db_conn.conn
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into books(title,author,publisher,category,isbn,stock,availability) values (%s,%s,%s,%s,%s,%s,%s)",[self.name.get(),self.author.get(),
                                                                                                                                        self.publisher.get(), self.category.get(),
                                                                                                                                        self.isbn.get(),self.stock.get(),ava])
                self.conn.commit() # Daten aus den Textfeldern entgegennehmen ([b.get(),c.get(),g]) und in die Datenbak schreiben

                messagebox.showinfo('Erfolg', "{} wurde hinzugefügt!".format(self.name.get())) #Infofenster bei Erfolg
                self.clear_book_gui()
                #ask = messagebox.askyesno("Info", "Möchten Sie ein weiteres Buch hinzufügen") # Noch ein Buch hinzufügen?

                
            except Error:
                messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbinduung mmit der DB fehl, Error Message
        

    def get_data(self):
            try:
                con = db_conn.conn
                cur = con.cursor()

                cur.execute("SELECT bookid, title, author, publisher, category, isbn, stock FROM books")
                rowdata = cur.fetchall()
                return rowdata
                
            except:
                messagebox.showerror("Fehler" , "Fehler bei der Datenbankverbindung!")
    
    def create_table(self):
        
        # Daten für die Spalten
        coldata = [
             {"text": "Buch ID", "stretch": False, "width":65},
             {"text": "Titel", "stretch": False, "width":200},
             {"text": "Autor", "stretch": False, "width":180},
             {"text": "Verlag", "stretch": False, "width":180},
             {"text": "Kategorie", "stretch": False, "width":150},
             {"text": "ISBN", "stretch": False, "width":120},
             {"text": "Verfügbar", "stretch": True, "width":100},
             ]

        rowdata = self.get_data()
        
        # Tabelle definieren
        books_table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            searchable=True,
            bootstyle=DARK,
            height=20,
            stripecolor=("#212121", "#ffffff"),
            pagesize=20
        )
        # Tabelle plazieren
        books_table.place(relx=0.01, rely=0.3)