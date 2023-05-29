from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(name='Apple pie', price=90, inventory=23)
        MenuItem.objects.create(name='Potato salad', price=120, inventory=40)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)