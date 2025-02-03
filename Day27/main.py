from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)



#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


#Button

def button_clicked():
    print("I got clicked")
    my_label["text"] = my_input.get()


my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

my_button2 = Button(text="New Button")
my_button2.grid(column=2, row=0)

#Entry
my_input = Entry(width="10")
my_input.grid(column=3, row=2)

window.mainloop()
