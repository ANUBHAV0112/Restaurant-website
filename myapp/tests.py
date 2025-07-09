from django.test import TestCase
from .models import Table, Booking
# Create your tests here.
# python manage.py test
class TableModelTest(TestCase):
    def test_table_str(self):
        table = Table.objects.create(name="Test Table")
        self.assertEqual(str(table), "Test Table")
        
 
class BookingModelTest(TestCase):
    def test_booking_str(self):
        table = Table.objects.create(name="Test Table")
        booking = Booking.objects.create(
            name="Test Booking",
            email="test@gmail.com",
            phone="1234567890",
            subject="Test Subject",
            message="This is a test booking message.",
        )
        # self.assertEqual(str(booking), "Test Booking - Test Table")
        self.assertEqual(str(booking), "Test Booking")