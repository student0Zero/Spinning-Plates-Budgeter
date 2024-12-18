from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Income
from .forms import IncomeForm

class IncomeViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        # Create a test income
        self.income = Income.objects.create(
            user=self.user,
            date='2024-12-08',
            in_amount=1000,
            description='Monthly salary',
            category='Salary',
        )

    def test_edit_income_get(self):
        # Test GET request to edit income view
        response = self.client.get(reverse('edit_income', args=[self.income.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'income/edit_income.html')
        self.assertIsInstance(response.context['form'], IncomeForm)

    def test_edit_income_post_valid(self):
        # Test POST request to edit income view with valid data
        data = {
            'date': '2024-12-09',
            'in_amount': 1500,
            'description': 'Year-end bonus',
            'category': 'Bonus',
        }
        response = self.client.post(reverse('edit_income', args=[self.income.id]), data)
        self.assertRedirects(response, reverse('view_income'))
        self.income.refresh_from_db()
        self.assertEqual(self.income.in_amount, 1500),
        self.assertEqual(self.income.description, 'Year-end bonus'),
        self.assertEqual(self.income.category, 'Bonus')

    def test_edit_income_post_invalid(self):
        # Test POST request to edit income view with invalid data
        data = {
            'date': '',
            'in_amount': '',
            'description': '',
            'category': '',
        }
        response = self.client.post(reverse('edit_income', args=[self.income.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_delete_income_get(self):
        # Test GET request to delete income view
        response = self.client.get(reverse('delete_income', args=[self.income.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'income/delete_income.html')

    def test_delete_income_post(self):
        # Test POST request to delete income view
        response = self.client.post(reverse('delete_income', args=[self.income.id]))
        self.assertRedirects(response, reverse('view_income'))
        self.assertFalse(Income.objects.filter(id=self.income.id).exists())

    def test_create_income_get(self):
        # Test GET request to create income view
        response = self.client.get(reverse('create_income'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'income/create_income.html')
        self.assertIsInstance(response.context['form'], IncomeForm)

    def test_create_income_post_valid(self):
        # Test POST request to create income view with valid data
        data = {
            'date': '2024-12-10',
            'in_amount': 500,
            'description': 'Django project',
            'category': 'Freelance',
        }
        response = self.client.post(reverse('create_income'), data)
        self.assertRedirects(response, reverse('view_income'))
        self.assertTrue(Income.objects.filter(category='Freelance', in_amount=500, user=self.user).exists())

    def test_create_income_post_invalid(self):
        # Test POST request to create income view with invalid data
        data = {
            'date': '',
            'in_amount': '',
            'description': '',
            'category': '',
        }
        response = self.client.post(reverse('create_income'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))