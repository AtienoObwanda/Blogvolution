from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators  import DataRequired, Length, Email,EqualTo, ValidationError
from flask_login import current_user
from ..models import User


class RegistrationForm(FlaskForm):
    '''
    Defines class for registration
    '''
    username = StringField('Username', 
                    validators=[DataRequired(),Length(min=4, max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                    validators=[DataRequired(),Length(min=6,max=12),
                    EqualTo('confirm_password',message = 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password',
                    validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already in use!')


    def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                    validators=[DataRequired(),Length(min=6,max=12)])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                    validators=[DataRequired(),Length(min=4, max=15)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    picture= FileField('Update profile picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already in use!')


    def validate_email(self, email):
        if email.data != current_user.email:
            user= User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already in use!')


class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])

    submit = SubmitField('Reset Password')

    def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email, kindly SIGNUP!')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                    validators=[DataRequired(),Length(min=6,max=12),
                    EqualTo('confirm_password',message = 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password',
                    validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Confirm Reset Password')
