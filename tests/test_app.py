import unittest
import unittest
from app.models import User,Comment,Post

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'new123')
    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('new123'))

class CommentsModelTest(unittest.TestCase):
    def setUp(self):
       self.new_comment = Comment(id=1, user_id = 1, comment = 'pin this',pitch_id = '6',date_posted='2022-05-08')
    def test_comment_variables(self):
       self.assertEquals(self.new_comment.comment,'pin this')
       self.assertEquals(self.new_comment.date_posted,'2022-05-08')
       self.assertEquals(self.new_comment.user_id, 1)
    def test_save_comment(self):
        self.assertTrue(len(Comment.query.all())>0)
        
class PostModelTest(unittest.TestCase):
    def test_save_pitch(self):
        self.assertTrue(len(Post.query.all())>0)