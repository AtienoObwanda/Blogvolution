from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, ValidationError
from flask_login import current_user




class PostForm(FlaskForm):
    
    title = StringField('Post Title',validators=[DataRequired()])

    content = TextAreaField('Post Content',validators=[DataRequired()])

    submit = SubmitField('Publish Post')