from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain

question_vault = []

for item in question_data:
    question_vault.append(
        QuestionModel(item["text"], item["answer"])
        )

print(len(question_vault))

quiz = QuizBrain(question_vault)

while quiz.questions_left() == True:
    quiz.next_question()


print("\nYou've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")