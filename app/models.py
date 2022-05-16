# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime

from . import db, login_manager

@login_manager.user_loader
def login_user(user_id):
    return User.query.get(int(user_id))


# Users
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author',lazy=True) #defining the one to many relationship btn post and author
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    likes =  db.relationship('Like',backref='user',lazy='dynamic')


def __repr__(self):
    return f'User({self.username}, {self.email},{self.image})'

class Post (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    datePosted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the post author
    comment =  db.relationship('Comment',backref='post',lazy='dynamic')
    likes =  db.relationship('Like',backref='post',lazy='dynamic')




def __repr__(self):
    return f"User({self.content},{self.datePosted})"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the user
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),nullable=False)
    comment = db.Column(db.String(100))




def __repr__(self):
    return f'User({self.comment})'


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #Id of the user
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),nullable=False)
   
# Quotes fetched from the api
class Quote:
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'