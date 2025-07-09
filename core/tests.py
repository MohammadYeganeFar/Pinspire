from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from core.models import Pin, Board
from account.models import CustomUser

class PinAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.pin_data = {
            'title': 'Test Pin',
            'description': 'A test pin',
            'owner': self.user.id,
            'visibility': 'PU',
        }

    def test_create_pin(self):
        url = reverse('pin-list')
        response = self.client.post(url, self.pin_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_pins(self):
        Pin.objects.create(title='Pin1', description='desc', owner=self.user, visibility='PU')
        url = reverse('pin-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class BoardAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser2', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.board_data = {
            'name': 'Test Board',
            'description': 'A test board',
            'owner': self.user.id,
            'visibility': 'PU',
        }

    def test_create_board(self):
        url = reverse('board-list')
        response = self.client.post(url, self.board_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_boards(self):
        Board.objects.create(name='Board1', description='desc', owner=self.user, visibility='PU')
        url = reverse('board-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1) 