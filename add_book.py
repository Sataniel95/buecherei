from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys

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
        isdn = StringVar()
        stock = StringVar()

        # Eingaben überprüfen
        def addBook():

            if len(name.get()) == 0 or len(author.get()) == 0 or len(publisher.get()) == 0 or len(category.get()) == 0 or len(isdn.get()) == 0 or len(stock.get()) == 0: # Ist eines der Eingabefelder leer?
                messagebox.showerror("Fehler","Bitte geben Sie einen Buchnamen/Autor an!")
            else:
                g = 'TRUE' # Verfügbarkeit des Buchs, wenn ein Buch neu eingepflegt wird, ist es auch logischerweise verfügbar
                try:
                    self.conn = mysql.connector.connect(host='localhost', # Verbindung mit der Datenbank aufbauen
                                         database='library_management',
                                         user='root',
                                         password='1234')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into books(name,author,publisher,cathegory,isdn,stock) values (%s,%s,%s,%s,%s,%s)",[name.get(),author.get(),publisher.get(), category.get(),isdn.get,amount.get])
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
        Label(self, text='').pack()

        Label(self, text='Buch hinzufügen:',bg='gray',fg='black',font=('Arial', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()

        Label(self, text='Buchname:',bg='gray',fg='black', font=('Arial', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=name, width=30).place(x=170, y=182)

        Label(self, text='Autor:',bg='gray',fg='black', font=('Arial', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=author, width=30).place(x=170, y=232)

        Label(self, text='Herausgeber:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=280)
        Entry(self, textvariable=publisher, width=30).place(x=170, y=282)

        Label(self, text='Kategorie:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=330)
        Entry(self, textvariable=category, width=30).place(x=170, y=332)

        Label(self, text='ISDN:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=380)
        Entry(self, textvariable=isdn, width=30).place(x=170, y=382)

        Label(self, text='Menge:', bg='gray', fg='black', font=('Arial', 10, 'bold')).place(x=60, y=430)
        Entry(self, textvariable=stock, width=30).place(x=170, y=432)

        Button(self, text="Hinzufügen", command=addBook).place(x=495, y=300)

AddBookWindow().mainloop()