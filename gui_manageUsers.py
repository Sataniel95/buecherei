import tkinter as tk
from tkinter import ttk as ttk, messagebox
import db_conn
from mysql.connector import Error
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import ttkthemes 
from gui_HoverButton import HoverButton
from PIL import Image, ImageTk 


class ManageUsers(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self,background="#1f1f1f").pack(expand= True, fill="both")
        self.place(x=256, y=0, relwidth=0.8, relheight=1)
        self.top_main_frame = tk.Frame(self, background="#1f1f1f" ,autostyle=False)
        self.top_main_frame.place(x=0, y=0, relwidth=1, relheight=0.4)
        self.menu_frame = tk.Frame(self.top_main_frame, background="#1f1f1f" ,autostyle=False)
        self.menu_frame.place(x=0, y=0, relwidth=0.58, relheight=1)
        self.info_frame = tk.Frame(self.top_main_frame, background="#1f1f1f" ,autostyle=False)
        self.info_frame.place(x=593, y=0, relwidth=0.4, relheight=1)
        
        
        self.topbg = tk.Label(self, bg="#141414", height=3, width=250, autostyle=False)
        self.topbg.place(x=593, y=0)
        
        self.logo_import = Image.open("img/users.png").resize((256,256))                     
        self.logo_tk = ImageTk.PhotoImage(self.logo_import)
        
        self.user_logo = ttk.Label(self, image=self.logo_tk, background="#1f1f1f")   
        self.user_logo.place(relx=0.15, rely=0.08)    
        
        self.create_table()
        self.create_menu()


    def create_menu(self):
        
        self.bglabel = tk.Label(self.menu_frame, bg="#141414", height=3, width=250, autostyle=False)
        self.bglabel.place(x=0, y=0)
        
        self.manage_user_btn1 = HoverButton(self.menu_frame, text="Benutzer hinzufügen", command=self.create_add_user_gui, bg="#141414",
                                        font=("Verdana" ,"15", "underline"), activebackground="#141414", 
                                        activeforeground="#df4807")
        self.manage_user_btn1.place(relx=0.03, rely=0.05)
        
        self.manage_user_btn2 = HoverButton(self.menu_frame, text="Benutzer bearbeiten", command=self.edit_user_gui, bg="#141414",
                                        font=("Verdana" ,"15", "underline"), activebackground="#141414", 
                                        activeforeground="#df4807")
        self.manage_user_btn2.place(relx=0.37, rely=0.05)
        
        self.manage_user_btn3 = HoverButton(self.menu_frame, text="Benutzer entfernen", command=self.delete_user, bg="#141414",
                                        font=("Verdana" ,"15", "underline"), activebackground="#141414", 
                                        activeforeground="#df4807")
        self.manage_user_btn3.place(relx=0.7, rely=0.05)
    
         
    def create_table(self):
                
        # Daten für die Spalten
        self.coldata = [
             {"text": "User ID", "stretch": False, "width":85},
             {"text": "Vorname", "stretch": False, "width":100},
             {"text": "Nachname", "stretch": False, "width":100},
             {"text": "Rolle", "stretch": False, "width":100},
             {"text": "E-Mail", "stretch": True, "width":610},
             ]

        self.rowdata = self.get_data()
        
        # Tabelle definieren
        self.user_table = Tableview(
            master=self,
            coldata=self.coldata,
            rowdata=self.rowdata,
            paginated=True,
            searchable=True,
            bootstyle=DARK,
            height=12,
            stripecolor=("#212121", "#ffffff"),
            pagesize=12
        )
        # Tabelle plazieren
        self.user_table.place(relx=0.01, rely=0.45)
        
        style = ttk.Style(self)                                                                                    
        ttkthemes.themed_style.ThemedStyle(theme="black")                                                           
        style.theme_use("black")                                                                                    
        style.configure("Treeview", background="#191717", fieldbackground="#191717", foreground="white", font="Verdana 10", rowheight=25)            
        style.configure('Treeview.Heading', background="#212121", foreground="white", borderwidth=0, font="Verdana 11 bold")   
        style.map('Treeview', background=[('selected', '#df4807')], foreground=[("selected", "white")])           


    def create_add_user_gui(self):        
        
        self.info_frame = tk.LabelFrame(self.top_main_frame,text="Benutzer hinzufügen", background="#1f1f1f", fg="white", font=("Verdana 15 bold"), autostyle=False)
        self.info_frame.place(x=593, y=55, relwidth=0.4, relheight=0.82)
        
        self.bglabel2 = tk.Label(self.top_main_frame, bg="#141414", height=3, width=250, autostyle=False)
        self.bglabel2.place(x=593, y=0)
        
        self.firstname = tk.StringVar() 
        self.lastname = tk.StringVar()
        self.role = tk.StringVar()
        self.email = tk.StringVar()
        
        OptionList = [
            "Administrator",
            "Mitarbeiter",
            "Student"
        ]
        self.role.set("Bitte wählen Sie eine Rolle")
        
        self.add_user_label1 = tk.Label(self.info_frame, text='Vorname:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.05)
        self.add_user_entry1 = tk.Entry(self.info_frame, textvariable=self.firstname, width=30)
        self.add_user_entry1.place(relx=0.5, rely=0.05)
        
        self.add_user_label2 = tk.Label(self.info_frame, text='Nachname:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.17)
        self.add_user_entry2 = tk.Entry(self.info_frame, textvariable=self.lastname, width=30)
        self.add_user_entry2.place(relx=0.5, rely=0.17)
        
        self.add_user_label3 = tk.Label(self.info_frame, text='Rolle:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.29)            
        self.add_user_entry3 = ttk.Combobox(self.info_frame, textvariable=self.role ,values=OptionList,width=26,state="readonly")
        self.add_user_entry3.place(relx=0.5, rely=0.29)

        self.add_user_label4 = tk.Label(self.info_frame, text='E-Mail:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.41)
        self.add_user_entry4 = tk.Entry(self.info_frame, textvariable=self.email, width=30)
        self.add_user_entry4.place(relx=0.5, rely=0.45)
        
       
        
        self.add_user_button = tk.Button(self.info_frame,
                                         text='Hinzufügen',
                                         relief="flat",
                                         bg="#df4807", 
                                         width=18, 
                                         font=('Verdana', 10),
                                         autostyle=False,
                                         command=self.add_user).place(relx=0.579,rely=0.79)

    
    def create_edit_info_frame(self):
        
        self.info_frame = tk.LabelFrame(self.top_main_frame, text="Benutzer aktualisieren", background="#1f1f1f", fg="white", font=("Verdana 15 bold"), autostyle=False)
        self.info_frame.place(x=593, y=55, relwidth=0.4, relheight=0.82)
        
        self.bglabel3 = tk.Label(self.top_main_frame, bg="#141414", height=3, width=250, autostyle=False)
        self.bglabel3.place(x=593, y=0)
        
        self.info_firstname = tk.StringVar() 
        self.info_lastname = tk.StringVar()
        self.info_role = tk.StringVar()
        self.info_email = tk.StringVar()
        
        self.info_id = tk.StringVar()
        
        OptionList = [
            "Administrator",
            "Mitarbeiter",
            "Student"
        ]
        
        self.info_frame_label1 = tk.Label(self.info_frame, text='Vorname:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.03)
        self.info_frame_entry1 = tk.Entry(self.info_frame, textvariable=self.info_firstname, width=30)
        self.info_frame_entry1.place(relx=0.5, rely=0.03)
        
        self.info_frame_label2 = tk.Label(self.info_frame, text='Nachname:',bg='#1f1f1f',fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.15)
        self.info_frame_entry2 = tk.Entry(self.info_frame, textvariable=self.info_lastname, width=30)
        self.info_frame_entry2.place(relx=0.5, rely=0.15)
        
        self.info_frame_label3 = tk.Label(self.info_frame, text='Rolle:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.27)
        self.info_frame_entry3 = ttk.Combobox(self.info_frame, textvariable=self.info_role ,values=OptionList,width=26)
        self.info_frame_entry3.place(relx=0.5, rely=0.27)

        self.info_frame_label4 = tk.Label(self.info_frame, text='E-Mail:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.39)
        self.info_frame_entry4 = tk.Entry(self.info_frame, textvariable=self.info_email, width=30)
        self.info_frame_entry4.place(relx=0.5, rely=0.43)
    
        
        self.info_frame_label5 = tk.Label(self.info_frame, text='ID:', bg='#1f1f1f', fg='white', font=('Verdana', 12, 'bold'),autostyle=False).place(relx=0.1, rely=0.75)
        self.info_frame_entry5 = tk.Entry(self.info_frame, textvariable=self.info_id, width=30)
        
        self.info_frame_entry5.place(relx=0.5, rely=0.75)
        
        self.info_frame_button = tk.Button(self.info_frame, 
                                                    text='Aktualisieren', 
                                                    width=18,                                                   
                                                    relief="flat",
                                                    bg="#df4807", 
                                                    font=('Verdana', 10),
                                                    command=self.edit_user_data, 
                                                    autostyle=False)
        self.info_frame_button.place(relx=0.579,rely=0.87)

        
    def forget_entry_frame(self):
         
         self.add_user_entry_frame.place_forget()

         
    def forget_info_frame(self):
         self.info_frame.place_forget()

    
    def clear_user_gui(self):
            
        self.add_user_entry1.delete(0,tk.END)
        self.add_user_entry2.delete(0,tk.END)
        self.add_user_entry3.delete(0,tk.END)
        self.add_user_entry4.delete(0,tk.END)
        

    
    def clear_info_frame(self):
            
        self.info_frame_entry1.delete(0,tk.END)
        self.info_frame_entry2.delete(0,tk.END)
        self.info_frame_entry3.delete(0,tk.END)
        self.info_frame_entry4.delete(0,tk.END)
        

    
    def add_user(self):

        if len(self.firstname.get()) == 0 or len(self.lastname.get()) == 0 or len(self.role.get()) == 0 or len(self.email.get()) == 0 : # Ist eines der Eingabefelder leer?
            messagebox.showerror("Fehler","Bitte füllen Sie alle Felder aus!")
        else:
            
            try:
                self.conn = db_conn.conn
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into users(firstname,lastname,role,email) values (%s,%s,%s,%s)",[self.firstname.get(),self.lastname.get(),
                                                                                                                                        self.role.get(), self.email.get()
                                                                                                                                        ])
                self.conn.commit() # Daten aus den Textfeldern entgegennehmen ([b.get(),c.get(),g]) und in die Datenbak schreiben

                messagebox.showinfo('Erfolg', "{} wurde hinzugefügt!".format(self.firstname.get())) #Infofenster bei Erfolg
                self.clear_user_gui()
                self.create_table()
                #ask = messagebox.askyesno("Info", "Möchten Sie ein weiteres Buch hinzufügen") # Noch ein Buch hinzufügen?

                
            except Error:
                messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbinduung mmit der DB fehl, Error Message


    def edit_user_data(self):
        try:
            self.conn = db_conn.conn
            self.myCursor = self.conn.cursor()
            self.myCursor.execute("UPDATE users SET firstname=%s, lastname=%s, role=%s, email=%s WHERE userid = %s", (self.info_firstname.get(),self.info_lastname.get(),
                                                                                                                                    self.info_role.get(), self.info_email.get(),
                                                                                                                                    self.info_id.get()))
            self.conn.commit() # Daten aus den Textfeldern entgegennehmen ([b.get(),c.get(),g]) und in die Datenbak schreiben
            self.create_table()
            self.forget_info_frame()
   

            messagebox.showinfo('Erfolg', "{} wurde aktualisiert!".format(self.info_firstname.get())) #Infofenster bei Erfolg
        except Error:
                messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbinduung mmit der DB fehl, Error Message

                
    def edit_user_gui(self):
                
        self.create_edit_info_frame()
        self.get_row_data()


    def delete_user(self):
         
            self.conn = db_conn.conn
            self.myCursor = self.conn.cursor()
            self.selected = self.user_table.get_rows(selected=True)
            self.selectedID = self.selected[0].values[0]
            self.selectedTitle = self.selected[0].values[1]
            self.warning = messagebox.askquestion('Achtung', 'Wollen Sie {} wirklich Löschen? '.format(self.selectedTitle), icon='warning')
            if self.warning == "yes":                
                self.myCursor.execute("DELETE FROM users WHERE userid = %s", [(self.selectedID)])
                self.conn.commit() 
                self.create_table()
                messagebox.showinfo('Erfolg', "{} wurde gelöscht!".format(self.selectedTitle)) #Infofenster bei Erfolg
            else:
                messagebox.showinfo('Info', "Löschvorgang abgebrochen")                          

        
    def get_data(self):

            try:
                con = db_conn.conn
                cur = con.cursor()

                cur.execute("SELECT userid, firstname, lastname, role, email FROM users")
                self.rowdata = cur.fetchall()
             
                return self.rowdata
                
            except:
                messagebox.showerror("Fehler" , "Fehler bei der Datenbankverbindung!")

      
    def get_row_data(self):
        
        self.row = self.user_table.get_rows(selected=True)
        
        
        self.info_frame_entry1.insert(0, self.row[0].values[1])
        self.info_frame_entry2.insert(0, self.row[0].values[2])
        self.info_frame_entry3.insert(0, self.row[0].values[3])
        self.info_frame_entry4.insert(0, self.row[0].values[4])
        self.info_frame_entry5.insert(0, self.row[0].values[0])
        self.info_frame_entry5.configure(state=tk.DISABLED)