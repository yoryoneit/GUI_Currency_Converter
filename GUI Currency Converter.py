import tkinter as tk


def currency_check():
    course_value.config(text=currency_value.get())


def calculate(event):
    label.config(text=currency_value.get() * float(amount_entry.get()))


root = tk.Tk()
root.title('Currency Converter')
root.geometry(f'280x200+300+300')

currency = tk.Label(root, text='Choose a currency:')
currency.grid(row=0, column=0, rowspan=2, stick='w')

currency_value = tk.DoubleVar()
currency_value.set(2.51)

usd = tk.Radiobutton(root, text='USD', variable=currency_value, value=2.51, command=currency_check)
usd.grid(row=0, column=1, stick='we')

eur = tk.Radiobutton(root, text='EUR', variable=currency_value, value=2.82, command=currency_check)
eur.grid(row=1, column=1, stick='we')

separator = tk.Label(root, text='------------------------------------------------------')
separator.grid(row=2, column=0, columnspan=2, stick='we')

course = tk.Label(root, text='Course (BYN):')
course.grid(row=3, column=0, stick='w')

course_value = tk.Label(root, text='2.51', fg='#DC143C')
course_value.grid(row=3, column=1, stick='we')

separator_1 = tk.Label(root, text='------------------------------------------------------')
separator_1.grid(row=4, column=0, columnspan=2, stick='we')

amount = tk.Label(root, text='Enter the amount:')
amount.grid(row=5, column=0, stick='w')

amount_entry = tk.Entry(root)
amount_entry.grid(row=5, column=1, stick='we')

separator_2 = tk.Label(root, text='------------------------------------------------------')
separator_2.grid(row=6, column=0, columnspan=2, stick='we')

convert = tk.Button(root, text='Convert to BYN')
convert.grid(row=7, column=0, stick='we')
convert.bind('<Button>', calculate)

label = tk.Label(root, text='', fg='#4682B4')
label.grid(row=7, column=1, stick='we')

root.mainloop()
