import tkinter as tk
from tkinter import ttk as ttk, messagebox
import db_conn
from mysql.connector import Error
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import ttkthemes 
from gui_HoverButton import HoverButton
from PIL import Image, ImageTk 


class ManageBooks(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self,background="#1f1f1f").pack(expand= True, fill="both")
        self.place(x=256, y=0, relwidth=0.8, relheight=1)
        self.top_main_frame = tk.Frame(self, background="#1f1f1f", autostyle=False)
        self.top_main_frame.place(x=0, y=0, relwidth=1, relheight=0.4)
        self.menu_frame = tk.Frame(self.top_main_frame, background="#1f1f1f", autostyle=False)
        self.menu_frame.place(x=0, y=0, relwidth=0.58, relheight=1)
        self.info_frame = tk.Frame(self.top_main_frame, background="#1f1f1f", autostyle=False)
        self.info_frame.place(x=593, y=0, relwidth=0.4, relheight=1)
        
        self.topbg = tk.Label(self, bg="#141414", height=3, width=250, autostyle=False)
        self.topbg.place(x=593, y=0)
        
        self.logo_import = Image.open("img/books.png").resize((204,204))                     
        self.logo_tk = ImageTk.PhotoImage(self.logo_import)
        
        self.books_logo = ttk.Label(self, image=self.logo_tk, background="#1f1f1f")   
        self.books_logo.place(relx=0.15, rely=0.12)                                     
        
        self.create_table()
        self.create_menu()


    def create_menu(self):
        # Hauptmenü oben
        self.bglabel = tk.Label(self.menu_frame, bg="#141414", height=3, width=250, autostyle=False)
        self.bglabel.place(x=0, y=0)
        
        self.manage_books_btn1 = HoverButton(self.menu_frame, text="Buch hinzufügen", command=self.create_add_book_gui, bg="#141414",
                                        font=("Verdana" ,"15", "underline"), activebackground="#141414", 
                                        activeforeground="#df4807")
        self.manage_books_btn1.place(relx=0.03, rely=0.05)
        
        self.manage_books_btn2 = HoverButton(self.menu_frame, text="Buch bearbeiten", command=self.edit_book_gui, bg="#141414",
                                        font=("Verdana" ,"15", "underline"), activebackground="#141414", 
                                        activeforeground="#df4807")
        self.manage_books_btn2.place(relx=0.37, rely=0.05)
        
        self.manage_books_btn3 = HoverButton(self.menu_frame, text="Buch entfernen", command=self.delete_book, bg="#141414",
                                        font=("Verdana" ,"15", "underline"), activebackground="#141414", 
                                        activeforeground="#df4807")
        self.manage_books_btn3.place(relx=0.7, rely=0.05)
    
        
         
    def create_table(self):
                                                                                                                                                
        # Daten für die Spalten
        self.coldata = [
             {"text": "Buch ID", "stretch": False, "width":75},
             {"text": "Titel", "stretch": False, "width":200},
             {"text": "Autor", "stretch": False, "width":180},
             {"text": "Verlag", "stretch": False, "width":180},
             {"text": "Kategorie", "stretch": False, "width":150},
             {"text": "ISBN", "stretch": False, "width":120},
             {"text": "Verfügbar", "stretch": True, "width":100},
             ]

        self.rowdata = self.get_data()
        
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


    def create_add_book_gui(self):        
        
        # Buch hinzufügen Menü, welches rechts oben erscheint, wenn man die Option wählt
        self.info_frame = tk.LabelFrame(self.top_main_frame,text="Buch hinzufügen", background="#1f1f1f", fg="white", font=("Verdana 15 bold"), autostyle=False)
        self.info_frame.place(x=593, y=55, relwidth=0.4, relheight=0.82)
        
        self.bglabel2 = tk.Label(self.top_main_frame, bg="#141414", height=3, width=250, autostyle=False)
        self.bglabel2.place(x=593, y=0)
        
        self.name = tk.StringVar() 
        self.author = tk.StringVar()
        self.publisher = tk.StringVar()
        self.category = tk.StringVar()
        self.isbn = tk.StringVar()
        self.stock = tk.StringVar()
        
        self.add_book_label1 = tk.Label(self.info_frame, text='Buchname:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.05)
        self.add_book_entry1 = tk.Entry(self.info_frame, textvariable=self.name, width=30)
        self.add_book_entry1.place(relx=0.5, rely=0.05)
        
        self.add_book_label2 = tk.Label(self.info_frame, text='Autor:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.17)
        self.add_book_entry2 = tk.Entry(self.info_frame, textvariable=self.author, width=30)
        self.add_book_entry2.place(relx=0.5, rely=0.17)
        
        self.add_book_label3 = tk.Label(self.info_frame, text='Verlag:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.29)
        self.add_book_entry3 = tk.Entry(self.info_frame, textvariable=self.publisher, width=30)
        self.add_book_entry3.place(relx=0.5, rely=0.29)

        self.add_book_label4 = tk.Label(self.info_frame, text='Kategorie:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.41)
        self.add_book_entry4 = tk.Entry(self.info_frame, textvariable=self.category, width=30)
        self.add_book_entry4.place(relx=0.5, rely=0.41)
        
        self.add_book_label5 = tk.Label(self.info_frame, text='ISBN:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.53)
        self.add_book_entry5 = tk.Entry(self.info_frame, textvariable=self.isbn, width=30)
        self.add_book_entry5.place(relx=0.5, rely=0.53)

        self.add_book_label6 = tk.Label(self.info_frame, text='Menge:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.65)
        self.add_book_entry6 = tk.Entry(self.info_frame, textvariable=self.stock, width=30)
        self.add_book_entry6.place(relx=0.5, rely=0.65)
        
        self.add_book_button = tk.Button(self.info_frame,
                                         text='Hinzufügen',
                                         relief="flat",
                                         bg="#df4807", 
                                         width=18, 
                                         font=('Verdana', 10),
                                         autostyle=False,
                                         command=self.add_book).place(relx=0.579,rely=0.79)

    
    def create_edit_info_frame(self):
        
        # Buch ändern Menü, welches rechts oben erscheint, wenn man die Option wählt
        self.info_frame = tk.LabelFrame(self.top_main_frame, text="Buch aktualisieren", background="#1f1f1f", fg="white", font=("Verdana 15 bold"), autostyle=False)
        self.info_frame.place(x=593, y=55, relwidth=0.4, relheight=0.82)
        
        self.bglabel3 = tk.Label(self.top_main_frame, bg="#141414", height=3, width=250, autostyle=False)
        self.bglabel3.place(x=593, y=0)
        
        self.info_name = tk.StringVar() 
        self.info_author = tk.StringVar()
        self.info_publisher = tk.StringVar()
        self.info_category = tk.StringVar()
        self.info_isbn = tk.StringVar()
        self.info_stock = tk.StringVar()
        self.info_id = tk.StringVar()
        
        
        self.info_frame_label1 = tk.Label(self.info_frame, text='Buchname:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.03)
        self.info_frame_entry1 = tk.Entry(self.info_frame, textvariable=self.info_name, width=30)
        self.info_frame_entry1.place(relx=0.5, rely=0.03)
        
        self.info_frame_label2 = tk.Label(self.info_frame, text='Autor:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.15)
        self.info_frame_entry2 = tk.Entry(self.info_frame, textvariable=self.info_author, width=30)
        self.info_frame_entry2.place(relx=0.5, rely=0.15)
        
        self.info_frame_label3 = tk.Label(self.info_frame, text='Verlag:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.27)
        self.info_frame_entry3 = tk.Entry(self.info_frame, textvariable=self.info_publisher, width=30)
        self.info_frame_entry3.place(relx=0.5, rely=0.27)

        self.info_frame_label4 = tk.Label(self.info_frame, text='Kategorie:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.39)
        self.info_frame_entry4 = tk.Entry(self.info_frame, textvariable=self.info_category, width=30)
        self.info_frame_entry4.place(relx=0.5, rely=0.39)
        
        self.info_frame_label5 = tk.Label(self.info_frame, text='ISBN:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.51)
        self.info_frame_entry5 = tk.Entry(self.info_frame, textvariable=self.info_isbn, width=30)
        self.info_frame_entry5.place(relx=0.5, rely=0.51)

        self.info_frame_label6 = tk.Label(self.info_frame, text='Menge:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.63)
        self.info_frame_entry6 = tk.Entry(self.info_frame, textvariable=self.info_stock, width=30)
        self.info_frame_entry6.place(relx=0.5, rely=0.63)
        
        self.info_frame_label7 = tk.Label(self.info_frame, text='ID:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.75)
        self.info_frame_entry7 = tk.Entry(self.info_frame, textvariable=self.info_id, width=30)
        
        self.info_frame_entry7.place(relx=0.5, rely=0.75)
        
        self.info_frame_button = tk.Button(self.info_frame, 
                                                    text='Aktualisieren', 
                                                    width=18,                                                   
                                                    relief="flat",
                                                    bg="#df4807", 
                                                    font=('Verdana', 10),
                                                    command=self.edit_book_data, 
                                                    autostyle=False)
        self.info_frame_button.place(relx=0.579,rely=0.87)

                   
    def create_add_book_entry_frame(self):
        
        self.add_book_entry_frame = tk.Frame(self.top_main_frame, background="#1f1f1f" ,autostyle=False)
        self.add_book_entry_frame.place(x=226, y=0, relwidth=0.3, relheight=1)

        
    def forget_entry_frame(self):
         
         self.add_book_entry_frame.place_forget()

         
    def forget_info_frame(self):
         
         self.info_frame.place_forget()

    
    def clear_book_gui(self):
            
        self.add_book_entry1.delete(0,tk.END)
        self.add_book_entry2.delete(0,tk.END)
        self.add_book_entry3.delete(0,tk.END)
        self.add_book_entry4.delete(0,tk.END)
        self.add_book_entry5.delete(0,tk.END)
        self.add_book_entry6.delete(0,tk.END)

    
    def clear_info_frame(self):
            
        self.info_frame_entry1.delete(0,tk.END)
        self.info_frame_entry2.delete(0,tk.END)
        self.info_frame_entry3.delete(0,tk.END)
        self.info_frame_entry4.delete(0,tk.END)
        self.info_frame_entry5.delete(0,tk.END)
        self.info_frame_entry6.delete(0,tk.END)

    
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
                self.create_table()
                

                
            except Error:
                messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbinduung mmit der DB fehl, Error Message


    def edit_book_data(self):
        try:
            self.conn = db_conn.conn
            self.myCursor = self.conn.cursor()
            self.myCursor.execute("UPDATE books SET title=%s, author=%s, publisher=%s, category=%s, isbn=%s, stock=%s WHERE bookid = %s", (self.info_name.get(),self.info_author.get(),
                                                                                                                                    self.info_publisher.get(), self.info_category.get(),
                                                                                                                                    self.info_isbn.get(),self.info_stock.get(),self.info_id.get()))
            self.conn.commit() 
            self.create_table()
            self.forget_info_frame()

            messagebox.showinfo('Erfolg', "{} wurde aktualisiert!".format(self.info_name.get())) #Infofenster bei Erfolg
        except Error:
                messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbindung mmit der DB fehl, Error Message

                
    def edit_book_gui(self):
             
        self.create_edit_info_frame()
        self.get_row_data()


    def delete_book(self):
         
            self.conn = db_conn.conn
            self.myCursor = self.conn.cursor()
            self.selected = self.books_table.get_rows(selected=True)
            self.selectedID = self.selected[0].values[0]
            self.selectedTitle = self.selected[0].values[1]
            self.warning = messagebox.askquestion('Achtung', 'Wollen Sie {} wirklich Löschen? '.format(self.selectedTitle), icon='warning')
            if self.warning == "yes":                
                self.myCursor.execute("DELETE FROM books WHERE bookid = %s", [(self.selectedID)])
                self.conn.commit() 
                self.create_table()
                messagebox.showinfo('Erfolg', "{} wurde gelöscht!".format(self.selectedTitle)) #Infofenster bei Erfolg
            else:
                messagebox.showinfo('Info', "Löschvorgang abgebrochen")                          

        
    def get_data(self):

            try:
                con = db_conn.conn
                cur = con.cursor()

                cur.execute("SELECT bookid, title, author, publisher, category, isbn, stock FROM books")
                self.rowdata = cur.fetchall()
               
                return self.rowdata
                
            except:
                messagebox.showerror("Fehler" , "Fehler bei der Datenbankverbindung!")

      
    def get_row_data(self):
        
        self.row = self.books_table.get_rows(selected=True)
        
        
        self.info_frame_entry1.insert(0, self.row[0].values[1])
        self.info_frame_entry2.insert(0, self.row[0].values[2])
        self.info_frame_entry3.insert(0, self.row[0].values[3])
        self.info_frame_entry4.insert(0, self.row[0].values[4])
        self.info_frame_entry5.insert(0, self.row[0].values[5])
        self.info_frame_entry6.insert(0, self.row[0].values[6])
        self.info_frame_entry7.insert(0, self.row[0].values[0])
        self.info_frame_entry7.configure(state=tk.DISABLED)