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

# while quiz.questions_left() == True:
#     quiz.next_question()


print("\nYou've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")