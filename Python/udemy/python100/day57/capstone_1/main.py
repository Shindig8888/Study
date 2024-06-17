from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_json = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template("index.html", posts= blog_json)

@app.route('/post/<blog_id>')
def read_post(blog_id):
    blog_id = int(blog_id)
    return render_template("post.html", id=blog_id, posts=blog_json)

if __name__ == "__main__":
    app.run(debug=True)
