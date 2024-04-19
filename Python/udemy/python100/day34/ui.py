from tkinter import *
from quiz_brain import Quizbrain
from data import question_data
import html

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self) -> None:
        self.score = 0
        #window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #canvas
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, highlightthickness=0)
        #canvas text
        self.quizbrain = Quizbrain(question_data)
        self.first_text = self.quizbrain.next_question()
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text=f"Q.{self.quizbrain.question_number}: {self.first_text}", font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #button image
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')


        #true button
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.guess_true)
        self.true_button.grid(column=0, row=2)

        #false button
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.guess_false)
        self.false_button.grid(column=1, row=2)

        #score label
        self.score_label = Label(bg=THEME_COLOR, text=(f"Score : 0"), font=('arial', 15,), fg='white')
        self.score_label.grid(column=1, row=0)

        self.window.mainloop()

    
    def config_question(self):
        '''generates question and print'''
        self.canvas.config(bg='white')
        question_string = self.quizbrain.next_question()
        if question_string!=0:
            self.canvas.itemconfig(self.canvas_text, text = f"Q{self.quizbrain.question_number}: {question_string}")
        else:
            self.canvas.config(bg=THEME_COLOR)
            self.canvas.itemconfig(self.canvas_text, fill='white', text=f"End of Question!\nYour Final Score is: {self.score}\n\nPress any button to exit!", font=('Arial', 15, 'bold'))
            self.true_button.config(command=self.window.destroy)
            self.false_button.config(command=self.window.destroy)


    def config_score(self):
        '''changing score'''
        self.score_label.config(text=f"Score : {self.score}")
    
    def guess_true(self):
        '''true_input'''
        guess = True
        is_right = self.quizbrain.check_answer(guess)
        self.guess_and_move_on(is_right)

    def guess_false(self):
        '''false_input'''
        guess = False
        is_right = self.quizbrain.check_answer(guess)
        self.guess_and_move_on(is_right)

    def guess_and_move_on(self, is_right):
        '''guess and generates next question'''
        if is_right:
            self.canvas.itemconfig(self.canvas_text, text=f"You are right!")
            self.canvas.config(bg='green')
            self.score+=1
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You are Wrong!")
            self.canvas.config(bg='red')
        self.window.after(300, self.config_question)
        
        self.config_score()

    def passing():
        '''do nothing function'''
        pass

