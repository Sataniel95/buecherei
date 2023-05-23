from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys
import db_conn

py = sys.executable

# Fenster erstellen
class AddBookWindow(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(480,560)
        self.minsize(480,560)
        self.title('Buch hinzufügen')
        self.canvas = Canvas(width=500, height=600, bg='gray')
        self.canvas.pack()

        name = StringVar() # Stringvars nehmen die Daten in den TExtfeldern entgegen, und packen Sie in eine Variable mit der wir weiterarbeiten können
        author = StringVar()
        publisher = StringVar()
        category = StringVar()
        isbn = StringVar()
        stock = StringVar()

        # Eingaben überprüfen
        def addBook():

            if len(name.get()) == 0 or len(author.get()) == 0 or len(publisher.get()) == 0 or len(category.get()) == 0 or len(isbn.get()) == 0 or len(stock.get()) == 0: # Ist eines der Eingabefelder leer?
                messagebox.showerror("Fehler","Bitte füllen Sie alle Felder aus!")
            else:
                ava = 'TRUE' # Verfügbarkeit des Buchs, wenn ein Buch neu eingepflegt wird, ist es auch logischerweise verfügbar
                try:
                    self.conn = db_conn.conn
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into books(name,author,publisher,category,isbn,stock,availability) values (%s,%s,%s,%s,%s,%s,%s)",[name.get(),author.get(),
                                                                                                                                         publisher.get(), category.get(),
                                                                                                                                         isbn.get(),stock.get(),ava])
                    self.conn.commit() # Daten aus den Textfeldern entgegennehmen ([b.get(),c.get(),g]) und in die Datenbak schreiben

                    messagebox.showinfo('Erfolg', "{} wurde hinzugefügt!".format(name.get())) #Infofenster bei Erfolg
                    ask = messagebox.askyesno("Info", "Möchten Sie ein weiteres Buch hinzufügen") # Noch ein Buch hinzufügen?

                    if ask:             # Wenn Ja:
                        self.destroy()  # Aktuelles fenster schliesen
                        os.system('%s %s' % (py, 'add_Book.py'))    # Und add_book wieder neu öffnen
                    else:
                        self.destroy() # Wenn Nein: "Buch hinzufügen" Fenster schließen
                except Error:
                    messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung!") # Schlägt die Verbinduung mmit der DB fehl, Error Message
        
        # Labels und Textfelder erstellen
        Label(self, text='').pack() #Leerzeile

        Label(self,text="Buch hinzufügen",bg='gray', font=("Arial",25,'bold')).place(relx= 0.5, rely= 0.1, anchor= CENTER)
        Label(self, text='').pack()

        Label(self, text='Buchname:',bg='gray',fg='black', font=('Arial', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=name, width=30).place(x=170, y=182)

        Label(self, text='Autor:',bg='gray',fg='black', font=('Arial', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=author, width=30).place(x=170, y=232)

        Label(self, text='Herausgeber:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=280)
        Entry(self, textvariable=publisher, width=30).place(x=170, y=282)

        Label(self, text='Kategorie:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=330)
        Entry(self, textvariable=category, width=30).place(x=170, y=332)

        Label(self, text='ISBN:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=380)
        Entry(self, textvariable=isbn, width=30).place(x=170, y=382)

        Label(self, text='Menge:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=430)
        Entry(self, textvariable=stock, width=30).place(x=170, y=432)

        Button(self, text='Hinzufügen', width=25, font=('Arial', 10), command=addBook).place(x=140,y=500)

AddBookWindow().mainloop()