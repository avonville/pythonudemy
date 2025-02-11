from tkinter import *
from random import choice
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

current_card = []

try:
    new_data = pandas.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"data\french_words.csv")
    word_list = data.to_dict(orient="records")
else:
    word_list = new_data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=card_back)

def known_word():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv(r"data\words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file=r"images\card_front.png")
card_back = PhotoImage(file=r"images\card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400,263,image=card_front)
title_text = canvas.create_text( 400,150, font=(FONT_NAME,40,"italic") )
word_text = canvas.create_text( 400,263, font=(FONT_NAME,80,"bold") )
canvas.grid(column=0, row=0, columnspan=2)

button_wrong_img = PhotoImage(file=r"images\wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(column=0, row=1)


button_right_img = PhotoImage(file=r"images\right.png")
button_right = Button(image=button_right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_word)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()
