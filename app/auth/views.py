import os
from flask import abort,request,redirect, render_template, url_for,flash
# from flask_login import login_user,current_user, logout_user, login_required
# import secrets
# from PIL import Image

# from ..sendMail import mail_message
# from .. import db,bcrypt
# from .form import RegistrationForm, LoginForm,UpdateAccountForm
# from ..models import User,Pitch

from . import auth



@auth.route('/register', methods=['GET','POST'])
def register():


    flash(f'Account created successfully!', 'success')
    # return redirect(url_for('auth.login'))
    
    return render_template("auth/register.html", title='BlogVolution-Login')