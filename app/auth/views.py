import os
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_user,current_user, logout_user, login_required
import secrets
# from PIL import Image

# from ..sendMail import mail_message
from .. import db,bcrypt
from .form import RegistrationForm, LoginForm,UpdateAccountForm
from ..models import User,Post

from . import auth


@auth.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        db.session.add(user) # add user
        db.session.commit() # commit session
        
        # mail_message("You have successfully signed up for a BlogVolution Splash account","email/welcome_user",user.email, user = user)

        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html", title='BlogVolution-Login',form=form)



@auth.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next') #  when user tries to acccess restricted page
            return redirect(next_page) if next_page else redirect(url_for('main.index')) # redirects to requested page after loggin in if it exists... if none, redirects to home page
        else:
            flash('Login Failed. Kindly check your email and password then try again','danger')
    return render_template("auth/login.html",form=form,title='BlogVolution-Login')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def save_picture(form_picture): # saving image
    random_hex = secrets.token_hex(8) # geneates new name for the picture
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('app/static/profile', picture_fn)
    
    #image resizing
    output_size=(125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path) # resized image

    return picture_fn


@auth.route('/account',methods=['GET', 'POST'])
@login_required #restricts the accoun page to only logged in users
def account():
    user_id = current_user._get_current_object().id
    post = Post.query.filter_by(user_id=user_id ).all()
    
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data) # seting picture 
            current_user.image = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Account details for {form.username.data} successfully updated!', 'sucess')
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username # Populate user username on to the form
        form.email.data = current_user.email # Populate user email on to the form
    image = url_for('static', filename='profile/' + current_user.image) # route for default profile picture
     
    return render_template("auth/account.html", title='Account', image=image, form=form,post=post)