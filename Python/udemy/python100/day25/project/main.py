from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.bgpic(r'blank_states_img.gif')
screen.setup(725,491)
data = pandas.read_csv(r'50_states.csv')
FONT = ('Arial', 8, 'normal')

while True:
    state_list = data.state.to_list()
    x_list = data.x.to_list()
    y_list = data.y.to_list()

    writer = Turtle()
    writer.penup()
    writer.hideturtle()

    score = 0

    is_game_on = True

    while is_game_on:

        if score == 0:
            answer = screen.textinput(f'{score}/50 States Correct', "Please enter state name: ").lower()
        else:
            answer = screen.textinput(f'{score}/50 States Correct', "What's another state name?: ")
        
        if answer == 'exit':
            break

        if answer.title() in state_list:
            answer_index = state_list.index(answer.title())
            writer.goto(x_list[answer_index], y_list[answer_index])
            writer.write(arg = f"{answer.title()}", move = True, align = 'center', font = FONT)
            del state_list[answer_index]
            del x_list[answer_index]
            del y_list[answer_index]
            score += 1
        else: continue

        if len(state_list) == 0:
            is_game_on = False

    dict_leftovers = {'leftover' : state_list}
    leftover_data = pandas.DataFrame(dict_leftovers)
    leftover_data.to_csv('Leftover States.csv')
    
    retry_answer = screen.textinput('Game End', "Congratulations! You win! Play again?(Y/N): ").lower()
    if retry_answer == 'y': 
        writer.clear()
        continue
    else: break
    
            

