class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def questions_left(self):
        if self.question_number < len(self.question_list):
            return True
        elif self.question_number == len(self.question_list):
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"\nQ.{self.question_number}: {question.text}. (True/False)?: ").title()
        self.check_answer(response, question.answer)

    def check_answer(self, response, question):
        if response == question:
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")
            print(f"Right answer was {question}")
        print(f"Your current score is {self.score}/{self.question_number}")
           