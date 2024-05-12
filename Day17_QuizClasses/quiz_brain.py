class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        while True:
            if(self.q_number == len(self.q_list)):
                print('Its done!')
                print(f'Your final score was {self.score}/{self.q_number}')
                break
            question = self.q_list[self.q_number]
            answer = input(f"Q.{self.q_number + 1}: {question.text} (True or False)?: ")
            self.check_answer(answer, question)
            self.q_number += 1

    def check_answer(self, answer, question):
        if answer.lower() == question.answer.lower():
            self.score += 1
            print('Correct')
            print(f'Your current score is {self.score}/{self.q_number + 1}')
        else:
            print('Wrong')
            print(f'The correct answer was: {question.answer}')
            print(f'Your current score is {self.score}/{self.q_number + 1}')
        print('')
