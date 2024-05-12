import pandas as pd
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'Day25_csv_pandas/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

rightAnswersCount = 0
rightAnswers = []
unAnsweredStates = []
data = pd.read_csv('Day25_csv_pandas/50_states.csv')

while rightAnswers != 50:
    answer_state = screen.textinput(title=f'{rightAnswersCount} /50 States Correct', prompt='Whats another states name?').title()

    if answer_state == 'Exit':
        for i in data.state.to_list():
            if i not in rightAnswers:
                unAnsweredStates.append(i)

        df = pd.DataFrame(unAnsweredStates).to_csv('Day25_csv_pandas/unAnsweredStates.csv')
        break

    if answer_state.title() in data.values:
        rightAnswersCount += 1
        rightAnswers.append(answer_state)
        pos = turtle.Turtle()
        state_data = data[data['state'] == answer_state]
        pos.penup()
        pos.setpos(int(state_data.x), int(state_data.y))
        pos.ht()
        pos.write(answer_state)
        pos.pendown()

print(unAnsweredStates)
# turtle.mainloop()
