from tkinter import *
import tkinter.messagebox as msg
import credentials as cr


# pip install mysql-connector-python
class Windows():
	def __init__(self, root):
		self.root = root
		self.root.geometry("400x400")
		self.root.title("Bücherrei Projekt")
		self.root.config(bg="red4")

		title = Label(self.root, text="Willkommen", bg="red4", font=("bold", "25"))
		title.pack()

		adminButton = Button(self.root, text="Admin", command=self.admin_page)
		adminButton.place(x=150, y=120)

		userButton = Button(self.root, text="Benutzer", command=self.user_page)
		userButton.place(x=150, y=180)

	def admin_page(self):
		adminWindow = Tk()
		adminWindow.title("Bücherverwaltung")
		adminWindow.geometry("400x400")
		adminWindow.config(bg="red4")

		book_name_label = Label(adminWindow, text="Buchname:", bg="red4", font=("bold", "15"))
		book_name_label.place(x=20, y=40)

		author_name_label = Label(adminWindow, text="Autor:", bg="red4", font=("bold", "15"))
		author_name_label.place(x=20, y=100)

		qty_label = Label(adminWindow, text="Anzahl:", bg="red4", font=("bold", "15"))
		qty_label.place(x=20, y=160)

		self.admin_book_entry = Entry(adminWindow)
		self.admin_book_entry.place(x=150, y=40)

		self.admin_author_entry = Entry(adminWindow)
		self.admin_author_entry.place(x=150, y=100)

		self.admin_qty_entry = Entry(adminWindow)
		self.admin_qty_entry.place(x=150, y=160)

		admin_submit = Button(adminWindow, text="Hinzufügen", command=self.admin_add)
		admin_submit.place(relx=0.5, rely=0.8, anchor=CENTER)

	def user_page(self):
		userWindow = Tk()
		userWindow.title("Buch ausleihen")
		userWindow.geometry("400x400")
		userWindow.config(bg="red4")

		user_book_label = Label(userWindow, text="Buchname:", bg="red4", font=("bold", "15"))
		user_book_label.place(x=20, y=40)

		user_author_label = Label(userWindow, text="Autor:", bg="red4", font=("bold", "15"))
		user_author_label.place(x=20, y=100)

		self.user_book_entry = Entry(userWindow)
		self.user_book_entry.place(x=150, y=40)

		self.user_author_entry = Entry(userWindow)
		self.user_author_entry.place(x=150, y=100)

		user_submit = Button(userWindow, text="Ausleihen", command=self.user_lend)
		user_submit.place(relx=0.5, rely=0.8, anchor=CENTER)

	def admin_add(self):
		import mysql.connector

		mydb = mysql.connector.connect(host="localhost", port=3306, user="root", password="3956", database="library_management")
		mycursor = mydb.cursor()

		bookname = self.admin_book_entry.get()
		author = self.admin_author_entry.get()
		qty = self.admin_qty_entry.get()

		mycursor.execute("insert into admin values(%s,%s,%s)", (bookname, author, qty))
		mydb.commit()
		msg.showinfo("Erfolg", "Buch wurde hinzugefügt!")

	def user_lend(self):
		import mysql.connector

		mydb = mysql.connector.connect(host="localhost", port=3306, user="root", password="3956",
									   database="library_management")
		mycursor = mydb.cursor()

		bookname = self.user_book_entry.get()
		author = self.user_author_entry.get()

		# mycursor.execute("inser into user values(%s,%s)",(bookname, author))
		mycursor.execute("select quantity from admin where Book_Name=%s and Author=%s", (bookname, author))

		q = 0
		for i in mycursor:
			q = int(i[0])
		if q >= 1:
			q = q - 1
			mycursor.execute("update admin set quantity=%s where Book_Name=%s and Author=%s", (q, bookname, author))
			mycursor.execute("insert into user values(%s,%s)", (bookname, author))
			mydb.commit()
			msg.showinfo("Erfolg", "Das Buch wurde ausgeliehen")
		else:
			msg.showerror("Fehler", "Buch nicht gefunden!")


root = Tk()
obj = Windows(root)
root.mainloop()
