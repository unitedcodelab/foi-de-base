from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post
from people.models import Student
from .utils.create_slug import create_slug


class PostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='12345'
        )
        self.student = Student.objects.create(
            user=self.user,
            name='Test User',
            email='test@test.com',
        )
        self.post = Post.objects.create(
            slug=create_slug(title='Test Post'),
            title='Test Post',
            content='Test Content',
            author=self.student,
        )

    def test_post_was_created(self):
        post = Post.objects.get(slug=self.post.slug)
        self.assertEqual(post, self.post)

