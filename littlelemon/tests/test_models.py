from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_add_item(self):
        item = Menu.objects.create(title="IceCream", price=2, inventory=30)
        self.assertEqual(str(item), "IceCream : £2 : 30")