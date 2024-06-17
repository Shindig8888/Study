from flask import Flask, render_template
import webbrowser
from threading import Timer
import random
from datetime import datetime as dt
import requests

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

app = Flask(__name__)



@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = dt.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/<name>")
def guess(name):
    parameter = {"name" : f"{name}"}

    gender_response = requests.get("https://api.genderize.io", params=parameter).json()
    age_response = requests.get("https://api.agify.io", params=parameter).json()

    gender = gender_response["gender"]
    age = age_response["age"]

    return render_template("guess.html", age = age, gender = gender, name = name)
    

@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_json = requests.get(blog_url).json()
    return render_template("blog.html", posts= blog_json)

if __name__ == "__main__":
    Timer(1, open_browser).start() 
    app.run(debug=True)

name = {"name" : "shindig"}





