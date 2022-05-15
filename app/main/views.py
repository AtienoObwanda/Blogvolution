from webbrowser import get
from flask import render_template,request,redirect,url_for
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_required,current_user

from .forms import PostForm
from . import main
from ..models import Post, User, Like, Comment, Quote
from .. import db
from ..requests import getPopular, getRandorm


# Views
@main.route('/')
def home():
    randormQuote = getRandorm()

    return render_template('index.html', randormQuote=randormQuote)


@main.route('/quotes')
def quotes():

    popularQuote =  getPopular()   
    return render_template('quotes.html', popularQuote = popularQuote)



@main.route('/all/posts')
def blog():
    name = "Time to get started "
    
    return render_template('blog.html', name=name)

@main.route('/contact')
def contact():
    name = "Time to get started "
    
    return render_template('contact.html', name=name)



@main.route('/post/new',methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post published successfully!','success')
        return redirect(url_for('main.home'))
    return render_template("post.html", form=form)


@main.route('/like/<post_id>/',methods = ['GET'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id)
    like = Like.query.filter_by(author= current_user.id, post_id=post_id).first()

    if not post:
        flash('Post not found',category='error')
    elif like:
        return redirect(url_for('main.index', post_id=post_id))
    else:
        like= Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    return redirect(url_for('main.blog'))
