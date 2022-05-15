from flask import render_template,request,redirect,url_for
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_required,current_user

from .forms import PostForm
from . import main
from ..models import Post
from .. import db
from . import main

# Views
@main.route('/')
def index():
    name = "Time to get started "
    
    return render_template('index.html', name=name)

@main.route('/post/new',methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        post=Post(category=form.category.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post published successfully!','success')
        return redirect(url_for('main.index'))
    return render_template("post.html", form=form)
