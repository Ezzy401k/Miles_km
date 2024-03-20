from tkinter import *

FONT = ("Arial", 15, "normal")

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=250, height=100)
window.maxsize(width=250, height=150)

entry = Entry(width=10)
entry.insert(index=0, string="0")
entry.grid(column=1, row=0)

label = Label(text="Miles", font=FONT)
label.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=FONT)
label_2.grid(column=0, row=1)

label_3 = Label(text="0", font=FONT)
label_3.grid(column=1, row=1)

label_4 = Label(text="Km", font=FONT)
label_4.grid(column=2, row=1)

label_6 = Label(text="0", font=FONT)
label_6.grid(column=1, row=2)

label_5 = Label(text="foot", font=FONT)
label_5.grid(column=2, row=2)


def convert():
    mile = float(entry.get())
    km = round(mile * 1.60934, 2)
    foot = round(mile * 5280, 2)
    label_3.config(text=f"{km}")
    label_6.config(text=f"{foot}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

window.mainloop()
