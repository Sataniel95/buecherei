import tkinter as tk
from tkinter import ttk as ttk, messagebox
import db_conn
from mysql.connector import Error
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import ttkthemes 
from gui_HoverButton import HoverButton
from PIL import Image, ImageTk

class Reminders(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self,background="#1f1f1f").pack(expand= True, fill="both")
        self.place(x=256, y=0, relwidth=0.8, relheight=1)
        self.top_main_frame = tk.Frame(self, background="#1f1f1f" ,autostyle=False)
        self.top_main_frame.place(x=0, y=0, relwidth=1, relheight=0.4)
        
        self.topbg = tk.Label(self, bg="#141414", height=3, width=250, autostyle=False)
        self.topbg.place(x=0, y=0)
        
        self.logo_import = Image.open("img/warning.png").resize((256,256))                     
        self.logo_tk = ImageTk.PhotoImage(self.logo_import)
        
        self.reminder_logo = ttk.Label(self, image=self.logo_tk, background="#1f1f1f")   
        self.reminder_logo.place(relx=0.15, rely=0.08)   