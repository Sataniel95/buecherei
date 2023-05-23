from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import db_conn

class Search(Tk):
    def __init__(self):
        super().__init__()
        searchBy = StringVar()
        searchTerm = StringVar()
        self.title("Buch suchen")
        self.maxsize(1200,500)
        self.minsize(1200,500)
        self.canvas = Canvas(width=1200, height=500, bg='gray')
        self.canvas.pack()

        Label(self,text="Buch suchen",bg='gray', font=("Arial",25,'bold')).place(relx= 0.5, rely= 0.1, anchor= CENTER)
        
        OptionList = [          #Variable mit einer Liste welche die Auswahloptionen enthält
            "Buch ID",
            "Buchname",
            "Autor",
            "Verlag",
            "ISBN",
        ]
        
        Label(self, text="Suche nach:",bg='gray', font=("Arial", 15, 'bold')).place(x=60, y=96)
        ttk.Combobox(self,textvariable=searchBy,values=OptionList,width=40,state="readonly").place(x = 190, y = 100)
        
        Label(self, text="Suchbegriff:",bg='gray', font=("Arial", 15, 'bold')).place(x=60, y=150)
        Entry(self,textvariable=searchTerm,width=43).place(x=190,y=155)
        
        def insert(data):                       # Funktion welche die Tabelle mit Daten füllt
            self.table.delete(*self.table.get_children()) # Wenn wir eine Suche starten, soll die Tabelle erst eimal geleert werden um Platz für neue Einträge zu schaffen
            for row in data: # for-schleife, welche die entgegengenommenen daten (später aus .fetchall) verarbeitet
                self.table.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[5], row[6])) # Daten in die tabelle einfügen. (ZeilenID, WOHIN, BezeichnungZeile, values->Werte der Felder 
        
        def search(): # Methode welche die Daten aus der DB anfragt und verarbeitet
            if (len(searchBy.get())) == 0: # Fehler wenn kein "Suche nach" ausgewählt wurde
                messagebox.showinfo('Fehler', 'Wählen Sie ein Suchkriterium aus')
            elif (len(searchTerm.get())) == 0: # Fehler wenn kein Suchbegriff eingegeben wurde
                messagebox.showinfo('Fehler', 'Bitte geben Sie einen Suchbegriff ein!')
 
            elif searchBy.get() == 'Buchname': # "Buchname" wurde als Suchkriterium ausgewählt und ein gültiger Suchbegriff gewählt
                try:
                    self.conn = db_conn.conn
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books where title LIKE %s",['%'+searchTerm.get()+'%']) # SQL-Statement. Gibt alle Einträge der books Tabelle zurück, 
                    self.data = self.mycursor.fetchall()                                                                                           
                                                                                                               # welche unseren Suchbegriff in der "name"-Spalte beinhalten
                    if self.data: # Die Antwort der DB überprüfen. Bei einem Treffer haben wir hier eine Liste mit den Daten                                                                             
                        insert(self.data) # Die Daten werden an die oben definierte "insert"-Funktion übergeben
                    else:
                        messagebox.showinfo("Fehler","Buch nicht gefunden!") # Wenn unsere Suche keinen Treffer beinhaltet, ist die Liste in "self.data" leer. Zeile 54 schlägt fehl und wir springen hier her
                except Error:
                    messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung")                    

            elif searchBy.get() == 'Autor':
                try:
                    self.conn = db_conn.conn
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books where author LIKE %s",['%'+searchTerm.get()+'%'])
                    self.data = self.mycursor.fetchall()
                    if self.data:
                        insert(self.data)
                    else:
                        messagebox.showinfo("Fehler","Buch nicht gefunden!")
                except Error:
                    messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung")
            
            elif searchBy.get() == 'Verlag':
                try:
                    self.conn = db_conn.conn
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books where publisher LIKE %s",['%'+searchTerm.get()+'%'])
                    self.data = self.mycursor.fetchall()
                    if self.data:
                        insert(self.data)
                    else:
                        messagebox.showinfo("Fehler","Buch nicht gefunden!")
                except Error:
                    messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung")
  
            elif searchBy.get() == 'ISBN':
                try:
                    self.conn = db_conn.conn
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from books where isbn LIKE %s",['%'+searchTerm.get()+'%'])
                    self.data = self.mycursor.fetchall()
                    if self.data:
                        insert(self.data)
                    else:
                        messagebox.showinfo("Fehler","Buch nicht gefunden!")
                except Error:
                    messagebox.showerror("Fehler","Fehler bei der Datenbankverbindung")        
        
        # "Suchen" Button der beim drücken die "search"-Funktion aufruft            
        Button(self,text="Suchen",width=15,bg='gray',font=("Arial",10,'bold'),command=search).place(x=460,y=148) 
        
        
        # Tabelle erstellen        
        self.table = ttk.Treeview(self, height=13,columns=("Name", "Autor", "Verlag", "ISBN", "Verfügbar"))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.table.yview) # Die Scrollbar erstellen
        self.table.configure(yscrollcommand=self.vsb.set) # Die Scrollbar an unsere Tabelle binden
        self.vsb.place(x=1005,y=200,height=287) # Position und Größe der Scrollbar festlegen
        self.table.heading("#0", text='Buch ID', anchor='center') # "heading" ist die Spaltenüberschrift. "#0" Ist die erste Spalte einer Zeile und dient intern als ID der Zeile. Wir nehmen unsere Buch-ID umd dieses Feld zu füllen
        self.table.column("#0", width=70, anchor='center') # Hier werden die erste Spalte definiert und mit "#0" der Spaltenüberschrift zugeordnet. (Wie in html beim Formular!) Zusätzlich wird die Standardbreite festgelegt und der Inhalt zentriert
        self.table.heading("Name", text='Name')
        self.table.column("Name", width=200, anchor='center')
        self.table.heading("Autor", text='Autor')
        self.table.column("Autor", width=200, anchor='center')
        self.table.heading("Verlag", text='Verlag')
        self.table.column("Verlag", width=200, anchor='center')
        self.table.heading("ISBN", text='ISBN')
        self.table.column("ISBN", width=200, anchor='center')
        self.table.heading("Verfügbar", text='Verfügbar')
        self.table.column("Verfügbar", width=90, anchor='center')
        self.table.place(x=40, y=200)
    
        ttk.Style().configure("Treeview", font=('Arial', 15)) # Schriftart der Tabelle festlegen

Search().mainloop()