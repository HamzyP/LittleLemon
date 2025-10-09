from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime

class MenuTest(TestCase):
    def test_add_item(self):
        item = Menu.objects.create(title="IceCream", price=2, inventory=30)
        self.assertEqual(str(item), "IceCream : £2 : 30")


class BookingTest(TestCase):
    def test_make_booking(self):
        test_name = "Bob"
        test_guests = 5
        # 2025 october 9th at 16:00
        test_date = datetime(2025, 10, 9, 16, 0)


        item = Booking.objects.create(name = test_name, no_of_guests=test_guests, bookingDate = test_date)
        expected_str = f"{test_name} for {test_guests} on {test_date.strftime('%Y-%m-%d')} at {test_date.strftime('%H:%M')}"
        self.assertEqual(str(item), expected_str)
