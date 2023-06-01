# import von externen Modulen
import tkinter as tk                              # Das Standard tkintermodul. Wir importieren es im dem Alias "tk"
from tkinter import ttk as ttk                    # Erweiterung für das tkinter Modul. Ermöglicht erweiterte Styling-Möglichkeiten für tkinter-Elemente
import customtkinter as ctk                       # Noch eine Erweiterung für tkinter. Sehr Umfangreiche Styling Möglichkeiten  
import ttkthemes                                  # Bibliothek für ttk welche schon voreingestellte "Themes" beinhaltet
# import von internen Modulen (unsere Dateien)
from gui_Sidebar import Sidebar                   # Unsere "Sidebar" Klasse. (Das Menü)
from gui_manageBooks import ManageBooks           # Unsere "ManageBooks" Klasse. (Bücher verwalten, im Menü)


# Die Klasse "Window" enthält alle grundlegenden Eigenschaften unseres Fensters. Sie dient dazu das Hauptfenster zu erstellen.
# Alle Inhalte sollen im Progammverlauf IN DIESES Fenster gepackt werden.
# Wir verwenden zur Erstellung des Fensters das Modul "customtkinter", es baut auf tkinter auf und bietet erweiterte Styling-Optionen, 
# welche im Standard tkinter nur sehr eingeschränkt zur Verfügung stehen


class Window(ctk.CTk):                                         # Wir defineiren die Klasse "Window" welche von der Klasse "CTk" aus (customtkinter) erbt
    def __init__(self):                                        
        
        # Grundeinstellungen
        super().__init__()                                     # "super().__init__()" hiermit erben wir alle Eigenschaften eines Ctk-Fensters (customtkinter)
        self.geometry("1280x720")                              # Die Größe des Fensters festlegen
        self.minsize(1280,720)                                 # Minimale Größe des Fensters festlegen
        self.maxsize(1280,720)                                 # Maximale Größe des Fensters festlegen
        self.title("SRH Bücherei")                             # Titel Fensters festlegen (Text der in der Windows-Titelleiste angezeigt wird)
        self.configure(fg_color="#191717")                     # Hiermit bestimmen wir die Hintergrundfarbe des Fensters. "#191717" ist ein HEX-Wert, man könnte aber auch Werte wie "black" oder RGB-Werte übergeben
        ctk.set_appearance_mode("dark")                        # Diese Zeile sorgt dafür, dass bestimmte Elemente wie z.B. die Titelleiste einen dunklen Stil bekommen
        
        
        # Elemente
        # In diesem Block nennen wir nun alle "Dinge" die wir beim öffnen unseres Fensters anzeigen wollen
        # Die einzelnen Elemente sind jeweils zur Übersichtlichkeit in anderen Dateien ausgelagert
        # Bisher gibt es die "Sidebar" welche das Menü auf der linken Seite des Fensters baut
        # Und die "manage_books" Seite. Sie wird im Moment als "Standart-Seite" beim starten des Programms geöffnet
        # Später wird man beim ersten öffnen des Fensters auf eine Willkommens-Seite geleitet und kann dann anhand des Menüs auswählen wohin man will
        self.sidebar = Sidebar(self)
        self.manage_books = ManageBooks(self)
        ##############################################################################################################################################
        # Styling
        # In diesem Block werden Styling-Optionen für alle Elemente festgelegt welche im Prgramm mit ttk erstellt werden.
        # Während man im Standard-tkinter modul (tk) den Style eines Elements direkt an dem Element selbst festlegt (Und man es somit auch für jedes Element selbst machen muss)
        # verfolgt ttk hier eher das Prinzip wie css im Webdesign. Jede Klasse welche ein ttk-Element baut (Frames, Buttons, Labels, etc...) besitzt ein Attribut names "style"
        # dieses kann von "ttk.Style" angesprochen werden und seine Werte daraus entgegenehmen. 
        # Somit können wir z.B ALLEN Buttons einen bestimmten Style zuweißen.
        style = ttk.Style(self)                                                                                     # Ein "Style-Objekt" erstellen
        ttkthemes.themed_style.ThemedStyle(theme="black")                                                           # Wir holen uns aus "ttkthemes" den vordefinierten Style "dark"
        style.theme_use("black")                                                                                    # Den "black" Style anwenden
        style.configure("Treeview", background="#191717", fieldbackground="#191717", foreground="white")            # In den nächsten 3 Zeilen werden nun einzelne Werte für die Tabelle (Treeview) gesetzt.
        style.configure('Treeview.Heading', background="#212121", foreground="white", borderwidth=0, font="bold")   # Auf diese Art können wir Einstellungen welche aus dem "black" Theme kommen, überschreiben
        style.map('Treeview', background=[('selected', '#df4807')], foreground=[("selected", "white")])             # Wir ändern z.B. die Hintergurndfarbe einer Tabelle (background), den Hintergrund der
                                                                                                                    # Spaltenüberschriften (Treeview.Heading background) oder die Farbe des aktuell ausgewählten
                                                                                                                    # Eintrags (selected)    
        
        # Das Fenster öffnen
        # "mainloop()" sorgt dafür, dass das Fenster nicht nur einmal geöffnet wird und sofort wieder verschwindet (Das python-script würde einmal durchlaufen und sich dann beenden)
        # "mainloop()" ist somit eine Schleife, die solange weiterläuft, bis wir sie beenden (Fenster schließen)
        self.mainloop()