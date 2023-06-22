# import von externen Modulen
import tkinter as tk
from tkinter import ttk as ttk                       
from PIL import Image, ImageTk                      # das PIL Modul bietet Funktionen um mit Bilddateien zu arbeiten. Wir verwenden es um unser Logo einzubinden
# import von internen Modulen (unsere Dateien)
from gui_HoverButton import HoverButton             # Unsere "HoverButton" Klasse. Zum erstellen von Buttons
from gui_manageBooks import ManageBooks
from gui_manageUsers import ManageUsers
from gui_lendBooks import LendBooks
from gui_requests import Requests
from gui_reminders import Reminders
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import ttkthemes 


# Die "Sidebar" Klasse definiert unser Auswahl-Menü an der linken Seite des Hauptfensters. Sie dient als Navigation. 
# Von hier aus sollen später einmal die hauptsächlichen Programmfunktionen erreichbar sein. Benutzer werden hier entsprechend ihrer Rolle, verschiedene Dinge sehen.

# Anhand von "ttk.Frame" innerhalb der Klammern, können wir erkennen, dass unsere Klasse eine Unterklasse von der Klasse "Frame" aus dem ttk-Modul ist.
# Frames sind in allen tkinter Modulen (tk,ttk,coustomtkinter...) essentielle und sehr wichtige Grundbausteine (Widgets) für die Gestaltung einer GUI.
# Frame bedeutet übersetzt Rahmen. Daher kann man sich schon sehr gut herleiten wozu sie eingesetzt werden.
# Frames bilden sogenannte "Container". Also klar definierte Bereiche innerhalb des Elements in welchem sie eingesetzt werden.
# Das anschaulichste Beispiel, worin man ein Frame einsetzen kann, ist ein Fenster. Das machen wir mit unserer Sidebar.
# Unsere "Sidebar" Klasse definiert also einen Rahmen in unserem Hauptfenster. Von dort aus ("gui_mainWindow") rufen wir sie dann auch (Zeile 37, gui_mainWindow).
# Ein Frame muss aber nicht unbedingt in ein Fenster gepackt werden. Es ist z.B. auch möglich und üblich ein Frame innerhalb eines anderen Frames zu plazieren.
# Dadurch kann man eine GUI strukturieren, also ein "Layout" erschaffen.

# Eine erste Auffälligkeit befindet sich im Konstruktor. def __init__(self, parent)
# Hier finden wir nicht nur das übliche "self" sonder auch noch "parent".
# Das das "parent" Attribut ist wichtig! An dieser Stelle wird festgehalten WER die Klasse gerufen hat. 
# Ein Frame kann nicht einfach so für sich alleine existieren, es MUSS immer irgendwo "reingepackt" werden.
# In userem Fall ist das "parent" (deutsch: Elternteil) unser Fenster (Window aus gui_mainWindow).
# Alles was über das Fenster bekannt ist wird in "parent" gespeichert. Das ist sehr wichtig, denn somit haben wir auch von dem Frame aus, Zugriff auf alle Eigenschaften des Fensters 

# Zudem besitzt unsere Sidebar Klasse auch noch eine weitere Funktion - "create_widgets()"
# In ihr wird das Erstellen (deshalb "create") der "Dinge" welche in das Frame gepackt werden sollen, verwirklicht.

class Sidebar(ttk.Frame):
    def __init__(self, parent):                                 # Wie oben beschrieben. Wir schaffen mit "parent" Platz für das Element welches unsere Klasse ruft
        super().__init__(parent)                                # Alles was das Objekt, welches uns gerufen hat in seinem Konstruktor besitzt, "holen" wir uns auch hier her
        self.place(x=0, y=0, relwidth=0.2, relheight=1)         # Hier wird angegeben WOHIN im Fenster das Frame plaziert werden soll. Genaueres dazu weiter unten innerhalb "create_widgets()"
        self.create_widgets()                                   # Wenn "Sidebar" gerufen wird, soll unser Frame auch gleich mit Inhalt gefüllt werden, dazu rufen wir die create_widgets() Methode
        
   
        
    def create_widgets(self):
        
        # Hier erst einmal ein wenig grundsätzliches zum erstellen und platzieren von Elementen (Widgets) mit tkinter
        # Alles was wir in unserem Fenster sehen können und irgendeine Funktion erfüllt, sei es tatsächlich funktional (Buttons, Eingabefelder, Tabellen...) oder auch nur visuell (Labels, Seperatoren...)
        # nennt man in tkinter Widgets.
        # Ein Widget kann erstellt werden indem man die entsprechende Klasse des Widgets aus dem dazugehörigen Modul ruft (z.b: "ttk.Label()")
        # Bei rufen der Klasse kann man in den Klammern gleich etliche Eigenschaften des Widgets festlegen.
        # Absolut notwendig ist IMMER mindestens ein Übergabeparamenter in der Klammer. Der erste Parameter bestimmt immer welchem übergeordneten Element das Widget gehört
        # In unserem Programm wird das fast immer "self" sein. Das heißt, das Widget gehört zu dem Element aus welcher Klasse es entstanden ist. Hier ist das "Sidebar"
        # Alle Widgets die hier entstehen gehören also zu unserem Sidebar-Frame
        
        # Die Vorgehensweise beim erstellen eines Widgets ist immer gleich: 
        # Zuerst erstellen eine Variable die auf das Widget zeigt wird -> (z.B. "self.background_label = ttk.Label()") (Das ist NICHT zwingend notwendig, aber im weiteren verlauf SEHR sinnvoll)
        # Nun ist das Widget zwar python-intern entstanden, damit wir es aber auch sehen könnnen, müssen wir ihm noch sagen wohin genau es sich plazieren soll
        # Dazu gibt es drei Möglichkeiten: ".pack", ".grid" und ".place"
        # .pack setzt ein Element standardmäßig an die nächste stelle an der Platz ist. Ohne weitere konfiguration tut es dies zentiret, von oben nach unten
        # Mit .grid kann man Elemente anhand eines Rasters anordnen. Man kann es sich vorstellen wie eine Tabelle mit Spalten und Zeilen
        # .grid ist in vielen Situationen eine sehr elegante Lösung um Elemente zu plazieren. Erfordert aber auch ein vielfaches an Aufwand im Gegensatz zu den beiden anderen Methoden
        # .place plaziert Elemente genau dahin, wo man es festlegt. Dabei können absolute Koordinaten genennt werden(x=,y=) oder auch relative Werte (relx=,rely=)
        
        # Das Hintergrund Label erstellen
        # Hier erstellen wir ein Label welches wir dazu nutzen den Hintergrund unserer Sidebar zu färben.
        # Man hätte dazu auch direkt den background des Frames ändern könnnen, ich wollte aber Zeigen wozu Labels verwendet werden können
        self.background_label = ttk.Label(self,background="#141414") # Ein Label und die dazugehörige Variable erstellen | self = Wem gehört das Label? Dem Frame! (self) | background setzt die Farbe des Labels
        self.background_label.pack(expand= True, fill="both") # Da das Label den Hintergurnd für das gesamte Frame darstellen soll, können wir es einfach mit .pack plazieren
                                                              # Standardmäßig sind Labels immer so groß wie sie sein müssen um ihren Inhalt darzustellen. Unser Label hat aber garkeinen Inhalt!
                                                              # Deshalb sagen wir ihm mit "expand=True" das es den GESAMTEN Paltz einnehmen soll der da ist. Und zwar in BEIDE Richtungen, auf der y- und x-Achse (fill="both")
        
        # Buttons definieren
        # Unsere Buttons werden durch die von uns erschaffene Klasse "Hoverbutton" definiert. Eine ausführliche Erklärung findet sich in gui_HoverButton.py
        # Die Paramenter "self" und "text" sollten selbsterklärend sein, "activeforeground" setzt hier die Farbe der Beschriftung des Buttons, wenn man die Maus über ihn plaziert.
        
        self.sidebar_btn1 = HoverButton(self, text="Benutzer verwalten", bg="#141414", activeforeground="#df4807", command=lambda: ManageUsers(self.master))
        self.sidebar_btn2 = HoverButton(self, text="Bücher verwalten", bg="#141414", activeforeground="#df4807", command=lambda: ManageBooks(self.master))
        self.sidebar_btn3 = HoverButton(self, text="Leihgaben", bg="#141414", activeforeground="#df4807", command=lambda: LendBooks(self.master))
        self.sidebar_btn4 = HoverButton(self, text="Anfragen", bg="#141414", activeforeground="#df4807", command=lambda: Requests(self.master))
        self.sidebar_btn5 = HoverButton(self, text="Mahnungen", bg="#141414", activeforeground="#df4807", command=lambda: Reminders(self.master))
        
        # Buttons plazieren
        self.sidebar_btn1.place(relx=0.1, rely=0.1, width=200, height=50)
        self.sidebar_btn2.place(relx=0.1, rely=0.2, width=200, height=50)
        self.sidebar_btn3.place(relx=0.1, rely=0.35, width=200, height=50)
        self.sidebar_btn4.place(relx=0.1, rely=0.45, width=200, height=50)
        self.sidebar_btn5.place(relx=0.1, rely=0.55, width=200, height=50)
        
        
        # Separatoren definieren und plazieren
        self.side_separator1 = ttk.Separator(self, orient='horizontal')
        self.side_separator1.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.001)
        
        side_separator2 = ttk.Separator(self, orient='horizontal')
        side_separator2.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.001)
        
        # Logo einbinden
        self.logo_import = Image.open("img/logo.png").resize((200,65))                     # Wir benutzen das PIL-Modul um aus der Bilddatei ein von Python verwendbares Objekt zu erzeugen.
        self.logo_tk = ImageTk.PhotoImage(self.logo_import)
        
        self.logo_label = ttk.Label(self, image=self.logo_tk, background="#141414")    # Nun erstellen wir wieder ein ttk.Label. Dieses Label kann das Bild-Objekt welches wir oben erstellt haben 
        self.logo_label.place(relx=0.1, rely=0.88)                                     # als Wert entgegennehmen. Somit können wir unser Logo einbinden.
        
