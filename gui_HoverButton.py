import tkinter as tk
from tkinter import ttk as ttk
import ttkthemes
# Hier wird in der "HoverButton"-Klasse ein Button definiert. 
# Es ist sinnvoll, ein Widget welches man in seinem Programm mehrfach verwendet, über eine Klasse zu definieren.
# Der GUI-Code in welcher der Button eingesetzt wird wird dadurch übersichtlicher und Änderungen welche man an einem Widget machen möchte, können dann in der Klasse global vorgenommen werden.

# Unser "HoverButton" erbt von der Standard-tkinter Button Klasse "Button". Im Konstruktor setzen wir gleich einige Standardwerte wie z.B. die Schriftart (font), die Farbe der Beschriftung (fg)
# oder auch die Breite des Rahmens (borderwidth="0") (Der Button wird dadurch rahemnlos)
# Zusätzlich ist im Konstruktor auch noch etwas Neues zu finden: "**kwargs". Hierauf würde ich gerne in Präsenz im Detail eingehen. Wer sich gerne schonmal im vorab informieren möchte kann nach
# "pyrhon *args **kwargs" googeln. 

# Dem HoverButton werden hier aber nicht nur Eigenschaften zugeteilt, er besitzt auch noch zwei Funktionen/Methoden. "on_enter" und "on_leave"
# Diese beiden Funktionen sorgen dafür, dass sich die Schriftfarbe des Buttons beim plazieren des Mauszeigers über dem Button, verändert. Wie genau das funktionier, wird unten erklärt

class HoverButton(tk.Button):
    def __init__(self, master, foreground="white", borderwidth="0", font="Verdana", activebackground="#232121", autostyle=False, **kwargs):
        tk.Button.__init__(self,  master=master, borderwidth="0", fg="white", font="Verdana", activebackground="#232121", autostyle=False, **kwargs)
        self.defaultForground = self["foreground"]
        self.bind("<Enter>", self.on_enter)                 # Die ".bind"-Methode kommt aus der "Button"-Klasse von tkinter. Sie sorgt dafür, dass wenn ein bestimmtes "event" (erster Paramenter in der Klammer)
                                                            # eintritt, etwas bestimmtes passiert (zweiter Paramenter in der Klammer).
                                                            # In unserem Fall bedeutet das, event <Enter> (der mauszeiger ist über dem Element) eintritt, dann soll unsere Funktion "on_enter" ausgeführt werden.
        self.bind("<Leave>", self.on_leave)                 # Das gleiche Prinzip gilt hier, wenn der Mauszeiger das Element wieder verlässt
        

    def on_enter(self, event):
        self['foreground'] = self['activeforeground']
        # Der Mauszeiger ist über dem Button:
        # Wir holen uns die aktuelle Farbe des Vodergrunds (Schriftfarbe) und setzen sie auf den Wert, welcher in activeforeground steht. activeforeground wird DIRKET dort definiert, wo der Button entsteht
        # z.B in gui_Sidebar Zeile 68
    def on_leave(self, event):
        self['foreground'] = self.defaultForground
        # Der Mauszeiger verlässt den Button
        # Wir nehmen den aktuellen Wert aus "foreground" (Der durch on_enter oben gesetzt wurde), und setzen ihn zurück auf den Standardwert welcher oben (Zeile 19) gesetzt wurde