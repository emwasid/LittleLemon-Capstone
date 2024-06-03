from django.test import TestCase
from .models import *

# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        
        self.assertEqual(itemstr, "IceCream : 80")

    def test_str(self):
        item = MenuItem.objects.create(title="Baklava", price=10, inventory=200)
        itemstr = item.__str__()
        
        self.assertEqual(itemstr, "Baklava")