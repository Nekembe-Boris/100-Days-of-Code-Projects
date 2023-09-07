from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain
from ui import QuizUi

question_vault = []

for item in question_data:
    question_vault.append(
        QuestionModel(item["question"], item["correct_answer"])
        )


quiz = QuizBrain(question_vault)
quiz_ui = QuizUi(quiz)

