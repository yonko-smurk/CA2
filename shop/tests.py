from django.test import TestCase
from django.urls import reverse
from .models import Category, Stock

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Outdoor Cushions',
            description='Outdoor cushions for your summer living space'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Outdoor Cushions')
        self.assertEqual(self.category.description, 'Outdoor cushions for your summer living space')

    def test_category_str_method(self):
        self.assertEqual(str(self.category.name), 'Outdoor Cushions')

    def test_category_get_absolute_url(self):
        expected_url = reverse('shop:stocks_by_category', args=[str(self.category.id)])
        self.assertEqual(self.category.get_absolute_url(), expected_url)

class StockModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Clothing',
            description='Fabulous clothing items'
        )

        self.stock = Stock.objects.create(
            name='Blouse',
            description='Silk long sleeve blouse',
            category=self.category,
            price=99.99,
            inventory=20,
            available=True
        )

    def test_stock_creation(self):
        self.assertEqual(self.stock.name, 'Blouse')
        self.assertEqual(self.stock.description, 'Silk long sleeve blouse')
        self.assertEqual(self.stock.category, self.category)
        self.assertEqual(self.stock.price, 99.99)
        self.assertEqual(self.stock.inventory, 20)
        self.assertTrue(self.stock.available)

    def test_stock_str_method(self):
        self.assertEqual(str(self.stock), 'Blouse')

    def test_stock_get_absolute_url(self):
        expected_url = reverse('shop:stock_detail', args=[str(self.category.id), str(self.stock.id)])
        self.assertEqual(self.stock.get_absolute_url(), expected_url) 

