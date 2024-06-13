from flask import Flask, redirect, url_for
import random


random_number = random.randint(1,9)

app = Flask(__name__)

@app.route("/reset")
def resetting_number():
    global random_number
    random_number = random.randint(1,9)
    return redirect(url_for('main_page'))

@app.route("/")
def main_page():
    return '<h1><b>Guess a number between 0 and 9</b></h1>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:number>")
def number_page(number):
    if number < random_number:
        return '<h1><font color="red"> Too low, try again!</font></h1>\
             <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2l4NDNibDdveTQxM3lxOWE3dzY1YWZ2eXY0eTkxaXF0Z2xjYzFxeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CM1rHbKDMH2BW/200.webp">\
                <h3>go to /reset to reset random number</h3>'
    elif number > random_number:
        return '<h1><font color="red"> Too high, try again!</font></h1>\
             <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWRpMzRma2U0b29tNXNnOTZzZHcxcmtrd3R3YzdzeHZpdXVxZHJxbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uUvyQdPSl8dhu/giphy.webp">\
                <h3>go to /reset to reset random number</h3>'
    else:
        return '<h1><font color="blue"> You found me!</font></h1>\
             <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmdxNWl2bmwwZXQ4NXRpMnF1NnZ0cW5ybXdpY24wbWRwaWMzcnJ2ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7SfAXqgRgh0li/giphy.webp">\
                <h3>go to /reset to reset random number</h3>'
    



if __name__ == "__main__":
    app.run(debug=True)