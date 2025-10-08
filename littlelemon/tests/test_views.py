from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient #used to simulate API requests.
from restaurant.serializers import MenuSerializer

class MenuViewPopulatedTest(TestCase):
    def setUp(self):
        Menu.objects.create(title= "burger", price=2.50, inventory=90)
        Menu.objects.create(title="cake", price=8.50, inventory=12)
    
    def test_getall(self):
        #simulate the request to the API
        client = APIClient()
        response = client.get('/restaurant/menu/')

        self.assertEqual(response.status_code, 200)

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.data, serializer.data)


#database needs to be empty hence no setUp func.
class MenuViewEmptyTest(TestCase):
    def test_getall_empty(self):
        client = APIClient()
        response = client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

