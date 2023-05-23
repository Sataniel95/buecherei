from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sys
import mysql.connector
from mysql.connector import Error
import db_conn

py = sys.executable


class AddUserWindow(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(500, 617)
        self.minsize(500, 617)
        self.title('Benutzer hinzufügen')
        self.canvas = Canvas(width=500, height=617, bg='gray')
        self.canvas.pack()
        firstname = StringVar()  # Variablen sinngemäß benannt
        lastname = StringVar()
        email = StringVar()
        role = StringVar()

        # Eingaben überprüfen
        def addUser():
            if len(firstname.get()) == 0 or len(lastname.get()) == 0 or len(email.get()) == 0 or len(
                    role.get()) == 0:  # Ist eines der Eingabefelder leer?
                messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus!")
            else:
                g = 'TRUE'  # Verfügbarkeit des Buchs, wenn ein Buch neu eingepflegt wird, ist es auch logischerweise verfügbar
                try:
                    self.conn = db_conn.conn
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into users (firstname,lastname,email,role) values (%s,%s,%s,%s)",
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

        # Labels und Textfelder erstellen
        Label(self, text='').pack()
        
        Label(self,text="Benutzer hinzufügen",bg='gray', font=("Arial",25,'bold')).place(relx= 0.5, rely= 0.1, anchor= CENTER)

        Label(self, text='').pack()
        
        Label(self, text='Vorname:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=firstname, width=30).place(x=170, y=182)
        
        Label(self, text='Nachname:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=lastname, width=30).place(x=170, y=232)
        
        Label(self, text='E-Mail:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=280)
        Entry(self, textvariable=email, width=30).place(x=170, y=282)
        
        Label(self, text='Rolle:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=330)

        OptionList = [
            "Administrator",
            "Mitarbeiter",
            "Kunde"
        ]
        role = StringVar(self)
        role.set("Bitte wählen Sie eine Rolle")

        ttk.Combobox(self,textvariable=role,values=OptionList,width=30,state="readonly").place(x=170, y=330)
        
        
        Button(self, text="Hinzufügen", command=addUser).place(x=210, y=400)

        



AddUserWindow().mainloop()
