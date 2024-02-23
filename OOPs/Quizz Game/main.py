from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    obj = Question(question['text'], question['answer'])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.question_number += 1
else:
    quiz.print_result()
