from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def instance(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")