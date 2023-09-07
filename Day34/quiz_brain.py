import html


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
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.question.text)
        return f"\nQ.{self.question_number}: {q_text}"

    def check_answer(self, response, question_res):
        if response == question_res:
            self.score += 1
            return True
        else:
            return False