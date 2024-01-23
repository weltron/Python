from tkinter import *

# Define a window
window = Tk()
window.title("Miles to Kilometer Conveter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

#Define an input entry box with a 0 placeholder
input = Entry(width=10)
input.insert(END, 0)
input.grid(column=1,row=0)

#A miles label aligned to grid
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#An equals to label aligned to grid
equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

#A conversion label to display answer aligned to grid 
conv_label = Label(text=0)
conv_label.grid(column=1, row=1)

#A km label aligned to grid
km_label = Label(text="KM")
km_label.grid(column=2, row=1)

#A function that calculates the conversion from miles to km
def calc_button():
    miles = float(input.get())
    km = miles * 1.61
    conv_label.config(text=km)

# A calculate button to execute the conversion
calc = Button(text="Calculate", command=calc_button)
calc.grid(column=1, row=2)

window.mainloop()