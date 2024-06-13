from flask import Flask

def make_bold(function):
    def wrapper():
        line = function()
        bold = '<b>'+line+'</b>'
        return bold
    return wrapper

def make_emphasis(function):
    def wrapper():
        line = function()
        empahsis = '<em>'+line+'</em>'
        return empahsis
    return wrapper

def make_underline(function):
    def wrapper():
        line = function()
        underline = '<u>'+line+'<u>'
        return underline
    return wrapper


app = Flask(__name__)

@app.route("/")
def main_page():
    return '<h1 style="text-align: center">hello!</h1>\
                <p>This is a paragraph</p>\
                <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmd0NHRkbjhqcTFkb2ZmeXJtdm9kMDljZWJvaGp0aXk4aWYyaHUzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yFQ0ywscgobJK/giphy.webp" width=200>'

@app.route("/<path:name>/<int:number>")
def greeting(name, number):
    return f"Hello {name.title()}, you are {number}years old!!!"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye."

if __name__ == "__main__":
    app.run(debug=True)