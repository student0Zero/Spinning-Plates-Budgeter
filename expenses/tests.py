from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Expense
from .forms import ExpenseForm
from decimal import Decimal


class ExpenseViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        # Create a test expense
        self.expense = Expense.objects.create(
            user=self.user,
            amount=Decimal('-100.00'),
            date='2024-12-08',
            description='Monthly salary',
            category='Food',
        )

    def test_edit_expense_get(self):
        # Test GET request to edit expense view
        response = self.client.get(reverse(
                'edit_expense', args=[self.expense.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expenses/edit_expense.html')
        self.assertIsInstance(response.context['form'], ExpenseForm)

    def test_edit_expense_post_valid(self):
        # Test POST request to edit expense view with valid data
        data = {
            'amount': Decimal('-150.00'),
            'date': '2024-12-09',
            'description': 'Bankers Bonus',
            'category': 'Big Money Payout',
        }
        response = self.client.post(reverse(
            'edit_expense',
            args=[self.expense.id]), data
            )
        self.assertRedirects(response, reverse('view_expenses'))
        self.expense.refresh_from_db()
        self.assertEqual(self.expense.amount, Decimal('-150.00'))
        self.assertEqual(self.expense.description, 'Bankers Bonus')
        self.assertEqual(self.expense.category, 'Big Money Payout')

    def test_edit_expense_post_invalid(self):
        # Test POST request to edit expense view with invalid data
        data = {
            'amount': '',
            'date': '',
            'description': '',
            'category': '',
        }
        response = self.client.post(reverse(
            'edit_expense',
            args=[self.expense.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_delete_expense_get(self):
        # Test GET request to delete expense view
        response = self.client.get(reverse(
            'delete_expense',
            args=[self.expense.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expenses/delete_expense.html')

    def test_delete_expense_post(self):
        # Test POST request to delete expense view
        response = self.client.post(reverse(
            'delete_expense',
            args=[self.expense.id]))
        self.assertRedirects(response, reverse('view_expenses'))
        self.assertFalse(Expense.objects.filter(id=self.expense.id).exists())

    def test_create_expense_get(self):
        # Test GET request to create expense view
        response = self.client.get(reverse('create_expense'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expenses/create_expense.html')
        self.assertIsInstance(response.context['form'], ExpenseForm)

    def test_create_expense_post_valid(self):
        # Test POST request to create expense view with valid data
        data = {
            'amount': Decimal('-200.00'),
            'date': '2024-12-10',
            'description': 'Freelance Django project',
            'category': 'Party Test Data',
        }
        response = self.client.post(reverse('create_expense'), data)
        self.assertRedirects(response, reverse('view_expenses'))
        self.assertTrue(Expense.objects.filter(
            category='Party Test Data',
            description='Freelance Django project',
            amount=Decimal('-200.00'),
            user=self.user).exists())

    def test_create_expense_post_invalid(self):
        # Test POST request to create expense view with invalid data
        data = {
            'amount': '',
            'date': '',
            'description': '',
            'category': '',
        }
        response = self.client.post(reverse('create_expense'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        