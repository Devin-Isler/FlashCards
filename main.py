from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WORDS = ("Ariel", 60, "bold")
LANGUAGE = ("Ariel", 40, "italic")
FR_to_EN_FILE = "data/french_words.csv"
CSV_FILE = "data/words_to_learn.csv"
word_number = 0
wait = ""


# ----------------------------------------FUNCTIONS----------------------------------------#
def select_card():
    global word_number, wait
    word_number = random.randint(0, len(data_dict))
    try:
        word = data_dict[word_number]
    except IndexError:
        pass
    else:
        front_letter = word[front_lang]
        back_letter = word[back_lang]
        front_card(front_letter)
        wait = window.after(3000, back_card, back_letter)


def front_card(word):
    cards.itemconfig(cards_image, image=front_image)
    cards.itemconfig(language_text, text=front_lang, fill="black")
    cards.itemconfig(word_text, text=word, fill="black")


def back_card(word):
    cards.itemconfig(cards_image, image=back_image)
    cards.itemconfig(language_text, text=back_lang, fill="white")
    cards.itemconfig(word_text, text=word, fill="white")


def right():
    window.after_cancel(wait)
    data_dict.pop(word_number)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv(CSV_FILE, index=False)
    select_card()


def wrong():
    window.after_cancel(wait)
    select_card()


# ------------------------------------------FILE------------------------------------------#
try:
    data = pandas.read_csv(CSV_FILE)
except FileNotFoundError:
    data = pandas.read_csv(FR_to_EN_FILE)
    data.to_csv(CSV_FILE, index=False)

data_dict = data.to_dict(orient="records")

languages = list(data.columns.to_list())
front_lang = languages[0]
back_lang = languages[1]


# --------------------------------------------UI-------------------------------------------#
window = Tk()
window.title("Flashy")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

cards = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
cards_image = cards.create_image(400, 263)
language_text = cards.create_text(400, 150, text="", font=LANGUAGE)
word_text = cards.create_text(400, 263, text="", font=WORDS)
cards.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=right)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=wrong)
wrong_button.grid(row=1, column=0)

select_card()

window.mainloop()
