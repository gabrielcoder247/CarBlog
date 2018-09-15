from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()],render_kw={"placeholder": "Title"})
    blog_data = TextAreaField('Type Blog here', validators=[Required()])
    photo_url = StringField('Photo URL', validators=[Required()], render_kw={'placeholder': 'Photo URL'})
    post = SubmitField('Post Blog')

class CommentForm(FlaskForm):
    name = StringField('Name',validators=[Required()],render_kw={"placeholder": "Name"})
    email = StringField('Email', validators=[Required()],render_kw={"placeholder": "Email"})
    comment_data = TextAreaField('Enter Comment', validators=[Required()],render_kw={"placeholder": "Comment"})
    post = SubmitField('Post Comment')

class EmailForm(FlaskForm):
    name = StringField('First Name', validators=[Required()],render_kw={"placeholder": "First Name"})
    email = StringField('Email', validators=[Required()],render_kw={"placeholder": "Email"})
    subscribe = SubmitField('Subscribe')
