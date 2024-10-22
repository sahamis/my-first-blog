from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User

class PostModelTests(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(
      username= "Test User",
      password = "password"
    )
  
  def test_create_post(self):
    post = Post(author=self.user, title="Sample title", text="Sample text")
    post.save()
    saved_post = Post.objects.get(author=self.user)
    self.assertEqual(saved_post.author, self.user)