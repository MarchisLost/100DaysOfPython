from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data['results']:
    question_bank.append(Question(i['question'], i["correct_answer"]))

qb = QuizBrain(question_bank)
qb.next_question()
