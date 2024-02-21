from django.test import TestCase
from .models import Customer, Order

class CustomerTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', code='123')

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.code, '123')

    def test_customer_str_representation(self):
        self.assertEqual(str(self.customer), 'John Doe')

class OrderTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', code='123')
        self.order = Order.objects.create(customer=self.customer, item='Product 1', amount=10.5)

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.item, 'Product 1')
        self.assertEqual(self.order.amount, 10.5)

    def test_order_str_representation_with_customer(self):
        self.assertEqual(str(self.order), 'Product 1 - John Doe')

    def test_order_str_representation_without_customer(self):
        self.order.customer = None
        self.assertEqual(str(self.order), 'Product 1 - Unknown')
