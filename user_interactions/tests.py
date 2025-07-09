from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user_interactions.models import Like, Comment
from account.models import CustomUser
from core.models import Pin

# Create your tests here.

class LikeAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='likeuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.pin = Pin.objects.create(title='Pin for Like', description='desc', owner=self.user, visibility='PU')
        self.like_data = {
            'user': self.user.id,
            'pin': self.pin.id,
        }

    def test_create_like(self):
        url = reverse('like-list')
        response = self.client.post(url, self.like_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_likes(self):
        Like.objects.create(user=self.user, pin=self.pin)
        url = reverse('like-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class CommentAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='commentuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.pin = Pin.objects.create(title='Pin for Comment', description='desc', owner=self.user, visibility='PU')
        self.comment_data = {
            'user': self.user.id,
            'pin': self.pin.id,
            'text': 'Nice pin!'
        }

    def test_create_comment(self):
        url = reverse('comment-list')
        response = self.client.post(url, self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comments(self):
        Comment.objects.create(user=self.user, pin=self.pin, text='Great!')
        url = reverse('comment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
