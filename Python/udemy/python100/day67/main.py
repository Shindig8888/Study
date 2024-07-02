from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

#CKeditor
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id, 
            'title': self.title,
           'subtitle': self.subtitle,
            'date': self.date,
            'body': self.body,
            'author': self.author,
            'img_url': self.img_url
        }

#WTForms
class NewPost(FlaskForm):
    blogtitle = StringField('Blog Post Title', [DataRequired()])
    subtitle = StringField('Subtitle', [DataRequired()])
    name = StringField('Your Name', [DataRequired()])
    image_url = StringField('Image URL', [DataRequired(), URL()])
    blog_content = CKEditorField('Blog Content', [DataRequired()])
    submit = SubmitField('Submit')
    
    def editpost(self, post: BlogPost):
        self.blogtitle.data = post.title
        self.subtitle.data = post.subtitle
        self.name.data = post.author
        self.image_url.data = post.img_url
        self.blog_content.data = post.body
        
    

    

    

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts_db = db.session.query(BlogPost).all()
    posts = [post.to_dict() for post in posts_db]
    
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    requested_post = db.session.query(BlogPost).filter_by(id=post_id).first()
    return render_template("post.html", post=requested_post.to_dict())


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = NewPost()
    if form.validate_on_submit():
        today = date.today()
        formatted_date = today.strftime("%B %d, %Y")
        new_post = BlogPost(
            title = form.blogtitle.data.title(),
            subtitle = form.subtitle.data.title(),
            author = form.name.data.title(),
            img_url = form.image_url.data,
            body = form.blog_content.data,
            date = formatted_date,
        )
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    target_post = db.session.query(BlogPost).filter_by(id=post_id).first()
    form = NewPost()
    if request.method == 'GET':  # GET 요청 시 기존 데이터로 폼 초기화
        form.editpost(target_post)

    elif form.validate_on_submit():
        target_post2 = db.session.query(BlogPost).filter_by(id=post_id).first()
        target_post2.title = form.blogtitle.data.title()
        target_post2.subtitle = form.subtitle.data.title()
        target_post2.author = form.name.data.title()
        target_post2.img_url = form.image_url.data
        target_post2.body = form.blog_content.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form, post_id=post_id)


@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    target = db.session.query(BlogPost).filter_by(id=post_id).first()
    db.session.delete(target)
    db.session.commit()
    flash('Post deleted!')
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
