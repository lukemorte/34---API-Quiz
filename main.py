from question_model import Question
from quiz_brain import QuizBrain
import requests


# constants, vars


TRIVIA_API = "https://opentdb.com/api.php"


# main code


def get_question_data():
    parameters = {
        "amount": 10,
        "type": "boolean",
    }
    response = requests.get(TRIVIA_API, parameters)
    response.raise_for_status()
    return response.json()["results"]


question_data = get_question_data()
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
