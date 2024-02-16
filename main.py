from question_model import Question
from data import get_questions
from quiz_brain import QuizBrain
from ui import QuizGUI


question_bank = []

def run_game():
    for question in get_questions()["results"]:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


run_game()
quiz = QuizBrain(question_bank)
gui = QuizGUI(quiz)

while quiz.still_has_questions():
    quiz.next_question()


