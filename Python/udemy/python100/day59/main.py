from flask import Flask, render_template
import requests
from pprint import pprint

app = Flask(__name__)
blog_json = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
pprint(blog_json)

@app.route('/')
def home():
    return render_template("index.html", posts= blog_json)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<blog_id>')
def post(blog_id):
    blog_index = int(blog_id)-1
    return render_template("post.html", article= blog_json[blog_index])



if __name__ == "__main__":
    app.run(debug=True)
