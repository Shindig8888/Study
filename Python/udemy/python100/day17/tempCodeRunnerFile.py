from data import question_data
from question_modeL import Question
from random import randint
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question.get("question")
    print(question_text)
    question_answer = question.get('correct_answer')
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)


A = QuizBrain(question_bank)

while A.still_has_question():
    A.next_question()

print('\nYou\'ve completed the quiz')
print(f'\nYour final score is: {A.point} / {A.question_number}')