from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

from rest_framework.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setup(self):
        MenuItem.objects.create(title='Item 1', price=10.99, inventory=10)
        MenuItem.objects.create(title='Item 2', price=15.99, inventory=5)
        MenuItem.objects.create(title='Item 3', price=8.99, inventory=20)
    
    def test_getall(self):
        response = self.client.get('/menu/')
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)