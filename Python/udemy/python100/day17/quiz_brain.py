class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.point = 0
        self.questions_list = questions_list
        from random import randint

    def still_has_question(self) -> bool:
        return len(self.questions_list) > 0


    def check_answer(self, user_answer, current_answer):

        if user_answer.lower() == current_answer.lower():
            print('You got it!')
            self.point += 1
        if user_answer.lower() != current_answer.lower():
            print(f"\nThat's wrong. The correct answer is : {current_answer}")
        print(f"\nYou got {self.point} / {self.question_number} right!")

    
    def next_question(self) -> str:
        self.question_number += 1
        from random import randint
        ranindex = randint(0,len(self.questions_list)-1)
        current_question = self.questions_list.pop(ranindex)
        while True:
            user_answer = input(f'\nQ. {self.question_number} : {current_question.text} (True/False) : ').lower()
            if user_answer == 'true' or user_answer == 'false':
                self.check_answer(user_answer, current_question.answer)
                break
            else:
                print('Please Enter True or False.')
                continue
        
   