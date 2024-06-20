from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("study.html")

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']
    print(name)
    print(password)
    return render_template('study2.html', name=name.title(), password=password)

if __name__ == "__main__":
    app.run(debug=True)