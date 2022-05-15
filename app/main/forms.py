from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, ValidationError
from flask_login import current_user




class PostForm(FlaskForm):
    
    title = TextAreaField('Content',validators=[DataRequired()])

    content = TextAreaField('Content',validators=[DataRequired()])

    submit = SubmitField('Publish Post')