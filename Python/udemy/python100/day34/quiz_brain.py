import html
class Quizbrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            return_value = html.unescape(self.current_question["question"])
            print(self.current_question['correct_answer'])
            return return_value
        else:
            return 0

    def check_answer(self, user_answer):
        correct_answer = self.current_question['correct_answer']
        if str(user_answer).lower() == correct_answer.lower():
            return True
        else:
            return False
