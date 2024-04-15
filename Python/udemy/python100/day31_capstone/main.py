from tkinter import *
import random
import pandas

BGCOLOR = '#AFDAC3'
language_foreign = 'Korean'
language_target = 'English'
guess_ox = None

data = pandas.read_csv('Korean_English.csv')

print(data)
row_lenth = data.shape[0]

print(row_lenth)
print(data.iloc[0].to_dict())

# #------------gen_random_word------------

def gen_random_word()->tuple:
    random_number = random.randint(0,row_lenth-1)
    ko_en_dict = data.iloc[random_number].to_dict()
    return ko_en_dict


#------------guess wrong------------
def guess_wrong():
    global guess_ox
    guess_ox = False
    return guessing(guess_ox)

#------------guess right------------
def guess_right():
    global guess_ox
    guess_ox = True
    return guessing(guess_ox)

#-----------guessing-------------
def guessing(guessOX):
    is_right = True
    ke_dict = gen_random_word()
    canvas_front.itemconfig(title_canvas, language_foreign)
    canvas_front.itemconfig(question_canvas, ke_dict[language_foreign])


    raise ValueError("function not set")

#------------ui------------


#window
window = Tk()
window.title('Flasgy')
window.config(padx=50, pady=50, bg = BGCOLOR)

#images
card_back = PhotoImage(file=r'images\card_back.png')
card_front = PhotoImage(file=r'images\card_front.png')
right_img = PhotoImage(file=r'images\right.png')
wrong_img = PhotoImage(file=r'images\wrong.png')

#canvas_front
canvas_front = Canvas(width=800, height=526, highlightthickness=0, bg= BGCOLOR)
canvas_front.create_image(400, 263, image=card_front)
title_canvas = canvas_front.create_text(400, 150, text = 'press any button to start', font = ('Ariel', 40, 'italic'))
question_canvas = canvas_front.create_text(400, 263, text = ' 환영합니다!', font = ('Ariel', 60, 'bold'))
question_canvas

canvas_front.grid(column=0, row=0, columnspan=2)


#wrong_button
wrong_button = Button(highlightthickness=0, command=guess_wrong, image=wrong_img)
wrong_button.grid(column=0,row=1)

#right_button
right_button = Button(highlightthickness=0, command=guess_right, image=right_img)
right_button.grid(column=1,row=1)












window.mainloop()