from data import question_data
from question_model import QuestionModel

question_vault = []

for item in question_data:
    question_vault.append(
        QuestionModel(item["text"], item["answer"])
        )

print(len(question_vault))

