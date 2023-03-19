from webbrowser import get
from flask import render_template,request,redirect,url_for
from flask import abort,request,redirect, render_template, url_for,flash
from flask_login import login_required,current_user

from .forms import PostForm,CommentForm
from . import main
from ..models import Post, User, Like, Comment, Quote
from .. import db
from ..requests import getRandorm #getPopular


# Views
@main.route('/')
def home():
    randormQuote = getRandorm()

    return render_template('index.html', randormQuote=randormQuote)


# @main.route('/quotes')
# def quotes():

#     # popularQuote =  getPopular()   
#     return render_template('quotes.html')



@main.route('/all/posts')
def blog():
    posts = Post.query.all()

    return render_template('blog.html', posts=posts)

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
        return redirect(url_for('main.blog'))
    return render_template("post.html", form=form)


@main.route('/like/<post_id>/',methods = ['GET'])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id)
    like = Like.query.filter_by(author= current_user.id, post_id=post_id).first()

    if not post:
        flash('Post not found',category='error')
    elif like:
        return redirect(url_for('main.home', post_id=post_id))
    else:
        like= Like(author=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()

    return redirect(url_for('main.blog'))

@main.route('/comment/<int:post_id>',methods = ['POST','GET'])
@login_required
def comment(post_id):
    post=Post.query.get_or_404(post_id)
    form = CommentForm()
    allComments = Comment.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
        postedComment = Comment(comment=form.comment.data,user_id = current_user.id, post_id = post_id)
        post_id = post_id
        db.session.add(postedComment)
        db.session.commit()
        flash('Comment added successfully')
        
        return redirect(url_for('main.comment',post_id=post_id))

    return render_template("comment.html",post=post, title='React to post!', form = form,allComments=allComments)

# Delete comment
@main.route('/delete/comment/<comment_id>')
@login_required

def deleteComment(comment_id):
    comment = Comment.query.filter(Comment.id == comment_id).first()

    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted!', 'success')
    return redirect(url_for('main.blog'))



@main.route('/delete/post/<int:post_id>',methods=['POST'])
@login_required
def deletePost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('main.post'))



@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def updatePost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post has been updated!', 'success')
        return redirect(url_for('main.blog', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('post.html', title='Update Post',
                           form=form, legend='Update Post')

# @main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
# @login_required
# def subscribe
