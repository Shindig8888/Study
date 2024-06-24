from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from dotenv import load_dotenv
import os
from flask_bootstrap import Bootstrap5



load_dotenv()
account_email = os.getenv("EMAIL")
account_password = os.getenv("PASSWORD")

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       email = form.email.data
       password = form.password.data
       if email == account_email and password==account_password:
            flash(f'Logged in as {email}', 'success')
            return redirect(url_for('success'))
       else:
            flash(f'Login denied as {email}', 'denied')
            return redirect(url_for('denied'))
    return render_template('login.html', form=form)

@app.route("/login/success")
def success():
    return render_template("success.html")

@app.route("/login/denied")
def denied():
    return render_template("denied.html")




if __name__ == '__main__':
    app.run(debug=True)