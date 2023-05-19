from tkinter import *
from tkinter import messagebox
import tkinter as tk
# from tkinter import filedialog             wird nicht verwendet
import os
import sys
import mysql.connector
from mysql.connector import Error

py = sys.executable

def checkEmail():
    if "@" is not in email.get():
        messagebox.showerror("Fehler", "Bitte geben Sie eine gültige E-Mail an!")  


class AddUserWindow(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Benutzer hinzufügen')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        firstname = StringVar()  # Variablen sinngemäß benannt
        lastname = StringVar()
        email = StringVar()
        role = StringVar()

        # Eingaben überprüfen
        
        def lenCheck(to_check):
            if len to_check == 0:
                messagebox.showerror("Fehler", "Bitte geben Sie einen Benutzer an!")
        
        
        
        
        def addUser():
            
            
            
            
            
            if len(firstname.get()) == 0 or len(lastname.get()) == 0 or len(email.get()) == 0 or len(
                    role.get()) == 0 or :  # Ist eines der Eingabefelder leer?
                messagebox.showerror("Fehler", "Bitte geben Sie einen Benutzer an!")
            else:
                g = 'TRUE'  # Verfügbarkeit des Buchs, wenn ein Buch neu eingepflegt wird, ist es auch logischerweise verfügbar
                try:
                    self.conn = mysql.connector.connect(host='localhost',  # Verbindung mit der Datenbank aufbauen
                                                        database='library_management',
                                                        user='root',
                                                        password='1234')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into users (firstname,lastname,email) values (%s,%s,%s,%s)",
                                          # books in useres geändert... das prinzip gilt für alle
                                          [firstname.get(), lastname.get(), email.get(), role.get()])  # ähnlichen Fälle
                    self.conn.commit()  # Daten aus den Textfeldern entgegennehmen ([b.get(),c.get(),g]) und in die Datenbak schreiben
                    messagebox.showinfo('Erfolg',
                                        "{} wurde hinzugefügt!".format(lastname.get()))  # Infofenster bei Erfolg
                    ask = messagebox.askyesno("Info",
                                              "Möchten Sie einen weiteren Benutzer hinzufügen")  # Noch ein Benutzer hinzufügen?
                    if ask:  # Wenn Ja:
                        self.destroy()  # Aktuelles fenster schliesen
                        os.system('%s %s' % (py, 'add_user.py'))  # Und add_book wieder neu öffnen
                    else:
                        self.destroy()  # Wenn Nein: "Buch hinzufügen" Fenster schließen
                except Error:
                    messagebox.showerror("Fehler",
                                         "Fehler bei der Datenbankverbindung!")  # Schlägt die Verbinduung mmit der DB fehl, Error Message
        
        
        
        
        
        
        def checkEmail():
            if "@" is not in email.get():
                messagebox.showerror("Fehler", "Bitte geben Sie eine gültige E-Mail an!") 
        
        
        
        # Labels und Textfelder erstellen
        Label(self, text='').pack()
        Label(self, text='Benutzer hinzufügen:', bg='gray', fg='black', font=('Arial', 20, 'bold')).place(x=150, y=70)

        Label(self, text='').pack()
        Label(self, text='Vorname:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=180)

        Entry(self, textvariable=firstname, width=30).place(x=170, y=182)
        Label(self, text='Nachname:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=230)

        Entry(self, textvariable=lastname, width=30).place(x=170, y=232)
        Label(self, text='E-Mail:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=280)

        Entry(self, textvariable=email, width=30).place(x=170, y=282)
        Button(self, text="Hinzufügen", command=addUser).place(x=245, y=330)

        OptionList = [
            "Administrator",
            "Mitarbeiter",
            "Kunde"
        ]

        app = tk.Tk()

        app.geometry('100x200')

        variable = tk.StringVar(app)
        variable.set(OptionList[0])

        opt = tk.OptionMenu(app, variable, *OptionList)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack()


AddUserWindow().mainloop()
