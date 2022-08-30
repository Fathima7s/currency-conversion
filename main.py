
from functools import partial
from tkinter import *


def validateLogin(username, password):

	import tkinter as tk
	import tkinter.messagebox

	root = tk.Tk()

	root.title("GUI : Currency Conversion")

	Tops = Frame(root, bg='#663420', pady=2, width=1850, height=100, relief="ridge")
	Tops.grid(row=0, column=0)

	headlabel = tk.Label(Tops, font=('times new roman', 24, 'bold'), text='\t \t Currency Converter  ', bg='#660000',
						 fg='white')
	headlabel.grid(row=1, column=0, sticky=W)

	variable1 = tk.StringVar(root)
	variable2 = tk.StringVar(root)

	variable1.set("Currency")
	variable2.set("Currency")

	# Function for converting a currency unit to another using the latest rate

	def RealTimeCurrencyConversion():
		from forex_python.converter import CurrencyRates
		c = CurrencyRates()

		from_currency = variable1.get()
		to_currency = variable2.get()

		if (Amount1_field.get() == ""):
			tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount.")

		elif (from_currency == "Currency" or to_currency == "Currency"):
			tkinter.messagebox.showinfo("Error !!", "Currency Not Selected.\n Please select FROM and TO Currency")

		else:
			new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
			new_amount = float("{:.2f}".format(new_amt))
			Amount2_field.insert(0, str(new_amount))

	def clear_all():
		Amount1_field.delete(0, tk.END)
		Amount2_field.delete(0, tk.END)

	CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "AUD"]

	root.configure(background='light blue')
	root.geometry("700x400")

	Label_1 = Label(root, font=('times new roman', 27, 'bold'), text="", padx=2, pady=2, bg="light blue", fg="black")
	Label_1.grid(row=1, column=0, sticky=W)

	label1 = tk.Label(root, font=('times new roman', 18, 'bold'), text="\tAmount  :", bg="white", fg="#660000")
	label1.grid(row=2, column=0, sticky=W)

	label1 = tk.Label(root, font=('times new roman', 18, 'bold'), text="\tFrom Currency  :", bg="white", fg="#660000")
	label1.grid(row=3, column=0, sticky=W)

	label1 = tk.Label(root, font=('times new roman', 18, 'bold'), text="\tTo Currency  :", bg="white", fg="#660000")
	label1.grid(row=4, column=0, sticky=W)

	label1 = tk.Label(root, font=('times new roman', 18, 'bold'), text="\tConverted Amount  :", bg="#660000",
					  fg="white")
	label1.grid(row=8, column=0, sticky=W)

	label_1 = Label(root, font=('times new roman', 7, 'bold'), text="", padx=2, pady=2, bg="light blue", fg="black")
	Label_1.grid(row=5, column=0, sticky=W)

	Label_1 = Label(root, font=('times new roman', 7, 'bold'), text="", padx=2, pady=2, bg="light blue", fg="black")
	Label_1.grid(row=7, column=0, sticky=W)

	FromCurrency_option = tk.OptionMenu(root, variable1, *CurrencyCode_list)
	ToCurrency_option = tk.OptionMenu(root, variable2, *CurrencyCode_list)

	FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
	ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

	Amount1_field = tk.Entry(root)
	Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

	Amount2_field = tk.Entry(root)
	Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

	Label_9 = Button(root, font=('courier', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="blue", fg="white",
					 command=RealTimeCurrencyConversion)
	Label_9.grid(row=6, column=0)

	Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg='light blue', fg="black")
	Label_1.grid(row=9, column=0, sticky=W)

	Label_9 = Button(root, font=('courier', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="white", fg="blue",
					 command=clear_all)
	Label_9.grid(row=10, column=0)

	root.mainloop()

	return

#window
tkWindow = Tk()
tkWindow.geometry('400x400')
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name", height=2, justify='center').grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username, justify='center').grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password", height=2).grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin, justify='center').grid(row=4, column=0)

tkWindow.mainloop()
