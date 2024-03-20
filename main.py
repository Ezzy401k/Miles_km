from tkinter import *  # Import all classes and functions from the tkinter module

# Define a font for the labels
FONT = ("Arial", 15, "normal")

# Create a tkinter window
window = Tk()
window.title("Mile to Km converter")  # Set the title of the window
window.minsize(width=250, height=100)  # Set the minimum size of the window
window.maxsize(width=250, height=150)  # Set the maximum size of the window

# Create an entry widget for inputting miles
entry = Entry(width=10)  # Set the width of the entry widget
entry.insert(index=0, string="0")  # Insert a default value of "0" into the entry widget
entry.grid(column=1, row=0)  # Place the entry widget in the window's grid layout

# Create a label to display "Miles"
label = Label(text="Miles", font=FONT)  # Set the text and font for the label
label.grid(column=2, row=0)  # Place the label in the window's grid layout

# Create a label to display "is equal to"
label_2 = Label(text="is equal to", font=FONT)
label_2.grid(column=0, row=1)

# Create a label to display the converted kilometers
label_3 = Label(text="0", font=FONT)
label_3.grid(column=1, row=1)

# Create a label to display "Km"
label_4 = Label(text="Km", font=FONT)
label_4.grid(column=2, row=1)

# Create a label to display the converted feet
label_6 = Label(text="0", font=FONT)
label_6.grid(column=1, row=2)

# Create a label to display "foot"
label_5 = Label(text="foot", font=FONT)
label_5.grid(column=2, row=2)


# Define a function to convert miles to kilometers and update the labels
def convert():
    mile = float(entry.get())  # Get the value entered in the entry widget and convert it to a float
    km = round(mile * 1.60934, 2)  # Convert miles to kilometers and round to 2 decimal places
    foot = round(mile * 5280, 2)  # Convert miles to feet and round to 2 decimal places
    label_3.config(text=f"{km}")  # Update the text of label_3 with the converted kilometers
    label_6.config(text=f"{foot}")  # Update the text of label_6 with the converted feet


# Create a button to trigger the conversion
button = Button(text="Calculate", command=convert)  # Set the text and command for the button
button.grid(column=1, row=3)  # Place the button in the window's grid layout

# Run the tkinter event loop
window.mainloop()
