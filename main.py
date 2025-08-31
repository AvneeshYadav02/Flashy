from tkinter import *
import pandas
import random
try:
    word_db = pandas.read_csv("./words_to_learn.csv")
except FileNotFoundError:
    word_db = pandas.read_csv("./french_words.csv")
finally:
    word_dict = word_db.to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"

#-----------------------------------[Functions]-----------------------------------#


def card_flip():
    canvas.itemconfig(language_text, text="English", fill="#000000")
    canvas.itemconfig(word_text, text=current_word["English"], fill="#000000")
    canvas.itemconfig(card_background, image=front_image)

def new_flashcard():
    global current_word, flipping_timer

    window.after_cancel(id=flipping_timer)

    try:
        current_word = random.choice(word_dict)
    except IndexError:
        pass
    else:
        canvas.itemconfig(language_text, text="French", fill="#FFFFFF")
        canvas.itemconfig(word_text, text=current_word["French"], fill="#FFFFFF")
        canvas.itemconfig(card_background, image=back_image)
        flipping_timer = window.after(3000, card_flip) 
       
def user_knows():
    global current_word

    word_dict.remove(current_word)

    new_flashcard()

    to_learn = pandas.DataFrame(word_dict)
    to_learn.to_csv("./words_to_learn.csv", index=False)

def user_doesnt_know():
    global current_word

    new_flashcard()



#-----------------------------------[Card_Canvas]-----------------------------------#


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipping_timer = window.after(3000, card_flip) 

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR , highlightthickness=0)

#Card
front_image = PhotoImage(file="./card_front.png")
back_image = PhotoImage(file="./card_back.png")
card_background = canvas.create_image(400, 263, image=back_image)

#Card_Text_Language
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))

#Card_Text_Word
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#-----------------------------------[Buttons]-----------------------------------#


check_image = PhotoImage(file="./right.png")
cross_image = PhotoImage(file="./wrong.png")

correct_button = Button(image=check_image,border=0, highlightthickness=0, command=user_knows)
correct_button.grid(column=1, row=1)

incorrect_button = Button(image=cross_image,border=0, highlightthickness=0, command=user_doesnt_know)
incorrect_button.grid(column=0, row=1)


new_flashcard()
window.mainloop()