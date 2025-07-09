from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from shop_manage.models import Product, Category
from account.models import CustomUser

class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='shopuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name='TestCat')
        self.product_data = {
            'name': 'Test Product',
            'description': 'A test product',
            'category': self.category.id,
            'price': 10.0,
            'is_available': True,
        }

    def test_create_product(self):
        url = reverse('product-list')
        response = self.client.post(url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_products(self):
        Product.objects.create(name='Product1', description='desc', category=self.category, price=5.0, is_available=True)
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']) if 'results' in response.data else len(response.data), 1)

class CategoryAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='catuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category_data = {
            'name': 'New Category',
        }

    def test_create_category(self):
        url = reverse('category-list')
        response = self.client.post(url, self.category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_categories(self):
        Category.objects.create(name='Cat1')
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1) 