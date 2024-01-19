"""
Test for comment app
!!!Due to delay I did hot enough tests and not nice by logic!!!!
"""

from django.test import TestCase, Client
from django.urls import reverse
from comment.models import Comment

from user.models import CustomUser

from captcha.conf import settings as captcha_settings

captcha_settings.CAPTCHA_TEST_MODE = True


class CommentAppTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpasswordSQ1'
        )
        self.client = Client()

    def test_comment_list_view(self):
        """Test for comment list view"""
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment/comment.html')
        self.assertTrue('comments' in response.context)

    def test_comment_creation_authenticated_user(self):
        """Test a creating of comment by authenticated user"""
        data = {
            'text': 'Test',
            "captcha_0": "8e10ebf60c5f23fd6e6a9959853730cd69062a15",
            "captcha_1": "PASSED",
        }
        url = reverse('index')
        self.client.login(username='testuser', password='testpasswordSQ1')

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(
            text='Test',
            author=self.user
        ).exists())

    def test_comment_creation_unauthenticated_user(self):
        """Test a creating of comment by unauthenticated user"""
        data = {
            'text': 'Test',
            "captcha_0": "8e10ebf60c5f23fd6e6a9959853730cd69062a15",
            "captcha_1": "PASSED",
        }
        url = reverse('index')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(
            text='Test comment text',
            author=self.user
        ).exists())

    def test_vote_karma_up(self):
        """Test for voting karma up"""
        self.comment = Comment.objects.create(
            author=self.user,
            text='TestPlus',
        )

        initial_karma = self.comment.karma

        self.client.force_login(self.user)

        response = self.client.post(
            reverse(
                'vote_karma',
                kwargs={'comment_id': self.comment.id, 'action': 'up'}
            )
        )

        self.assertEqual(response.status_code, 200)

        updated_comment = Comment.objects.get(pk=self.comment.id)

        self.assertEqual(updated_comment.karma, initial_karma + 1)

    def test_vote_karma_down(self):
        """Test for voting karma down"""
        self.comment = Comment.objects.create(
            author=self.user,
            text='TestMinus',
        )
        initial_karma = self.comment.karma

        self.client.force_login(self.user)

        response = self.client.post(
            reverse(
                'vote_karma',
                kwargs={'comment_id': self.comment.id, 'action': 'down'})
        )

        self.assertEqual(response.status_code, 200)

        updated_comment = Comment.objects.get(pk=self.comment.id)

        self.assertEqual(updated_comment.karma, initial_karma - 1)
