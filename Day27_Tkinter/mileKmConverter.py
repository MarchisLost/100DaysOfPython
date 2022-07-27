from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# Label
myLabel1 = Label(text='Miles')
myLabel1.grid(column=2, row=0)
myLabel2 = Label(text='is equal to')
myLabel2.grid(column=0, row=1)
myLabel3 = Label(text='Km')
myLabel3.grid(column=2, row=1)
myLabel4 = Label(text='0')
myLabel4.grid(column=1, row=1)


def buttonClicked():
    km = float(entry.get()) * 1.609344
    myLabel4.config(text=km)


# Button
button = Button(text='Calculate', command=buttonClicked)
button.grid(column=1, row=2)

# Entries
entry = Entry(width=5)
# Add some text to begin with 
entry.insert(END, string="0")
# Gets text in entry
entry.grid(column=1, row=0)

window.mainloop()
