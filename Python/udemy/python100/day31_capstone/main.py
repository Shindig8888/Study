from tkinter import *
import random
import pandas

BGCOLOR = '#AFDAC3'
language_foreign = 'Korean'
language_target = 'English'
guess_ox = None
score = 0
timer = None
round = 0
percentage = None
ke_list = []

try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('Korean_English.csv')

data_dict = data.to_dict()

# #------------gen_random_word------------

def gen_random_word()->list:
    #generating randome word
    global percentage
    percentage = random.randint(0,1)
    print(percentage)
    #50% chance to generate correct Korean-English pair
    if percentage == 0:
        random_number = random.randint(0,len(data_dict['Korean'])-1)
        korean = data_dict['Korean'][random_number]
        english = data_dict['English'][random_number]
        return [random_number, korean, english]
    else:
        random_number = random.randint(0,len(data_dict['Korean'])-1)
        korean = data_dict['Korean'][random_number]
        another_number = random.randint(0,len(data_dict['Korean'])-1)
        english = data_dict['English'][another_number]
        return [random_number, korean, english]

#flickering


#------------guess wrong------------
def guess_wrong():
    #if wrong button got clicked
    global guess_ox
    global ke_list
    if round != 0:
        guess_ox = False
        guessing(guess_ox)
    gen_and_set()

#------------guess right------------
def guess_right():
    #if right button got clicked
    global guess_ox
    global ke_list
    if round != 0:
        guess_ox = True
        guessing(guess_ox)
    gen_and_set()


#-----------gen_and_set-------------
def gen_and_set():
    #generate random word and change canvas
    global timer
    global round
    global ke_list
    if len(data_dict['Korean']) != 0:
        canvas.itemconfig(score_canvas, text = f'score: {score}, {len(data_dict["Korean"])} left')
        if round != 0:
            window.after_cancel(timer) #reset canvas

        ke_list = gen_random_word()

        canvas.itemconfig(canvas_image, image = card_front)
        canvas.itemconfig(title_canvas, text = language_foreign)
        canvas.itemconfig(question_canvas, text = ke_list[1])

        timer = window.after(3000, turn_card, ke_list)

        round+=1

    else:
        canvas.itemconfig(title_canvas, text = 'You win!')
        canvas.itemconfig(question_canvas, text = '게임 종료!')
        canvas.itemconfig(score_canvas, text = '수고하셨습니다!')

#-----------guessing-------------
def guessing(guessOX):
    global score
    global data_dict
    key_number = ke_list[0]

    if percentage == 0 and guessOX==True:
        del data_dict['Korean'][key_number]
        del data_dict['English'][key_number]
        score+=1
    elif percentage==1 and guessOX==False:
        del data_dict['Korean'][key_number]
        del data_dict['English'][key_number]
        score+=1
    else:
        pass

#---------------turn_card-------------
def turn_card(ke_list):
    english_word = ke_list[2]
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_canvas, text= language_target, fill="black")
    canvas.itemconfig(question_canvas, text= english_word, fill="black")

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
canvas = Canvas(width=800, height=526, highlightthickness=0, bg= BGCOLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
title_canvas = canvas.create_text(400, 150, text = 'press any button to start', font = ('Ariel', 40, 'italic'))
question_canvas = canvas.create_text(400, 263, text = ' 환영합니다!', font = ('Ariel', 60, 'bold'))
score_canvas = canvas.create_text(400, 340, text = '아무키나 눌러주세요!', font = ('Ariel', 20, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)


#wrong_button
wrong_button = Button(highlightthickness=0, command=guess_wrong, image=wrong_img)
wrong_button.grid(column=0,row=1)

#right_button
right_button = Button(highlightthickness=0, command=guess_right, image=right_img)
right_button.grid(column=1,row=1)


#loop end
window.mainloop()

#after roop(program end), file saves
words_remaining = pandas.DataFrame(data_dict)
words_remaining.to_csv('words_to_learn.csv')

words_right = pandas.concat([words_remaining, data]).drop_duplicates(keep=False)

try:
    existing_data = pandas.read_csv('words_correct.csv')
    
except FileNotFoundError:
    words_right.to_csv('words_correct.csv')
else:
    words_right_tosave = pandas.concat([existing_data, words_right], ignore_index=True)
    words_right_tosave.to_csv('words_correct.csv')

    