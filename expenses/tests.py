from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Expense
from .forms import ExpenseForm

class ExpenseViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        # Create a test expense
        self.expense = Expense.objects.create(
            user=self.user,
            category='Food',
            amount=100,
            date='2023-12-08'
        )

    def test_edit_expense_get(self):
        # Test GET request to edit expense view
        response = self.client.get(reverse('edit_expense', args=[self.expense.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expenses/edit_expense.html')
        self.assertIsInstance(response.context['form'], ExpenseForm)

    def test_edit_expense_post_valid(self):
        # Test POST request to edit expense view with valid data
        data = {
            'category': 'Transport',
            'amount': 150,
            'date': '2023-12-09'
        }
        response = self.client.post(reverse('edit_expense', args=[self.expense.id]), data)
        self.assertRedirects(response, reverse('view_expenses'))
        self.expense.refresh_from_db()
        self.assertEqual(self.expense.category, 'Transport')
        self.assertEqual(self.expense.amount, 150)

    def test_edit_expense_post_invalid(self):
        # Test POST request to edit expense view with invalid data
        data = {
            'category': '',
            'amount': '',
            'date': ''
        }
        response = self.client.post(reverse('edit_expense', args=[self.expense.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_delete_expense_get(self):
        # Test GET request to delete expense view
        response = self.client.get(reverse('delete_expense', args=[self.expense.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expenses/delete_expense.html')

    def test_delete_expense_post(self):
        # Test POST request to delete expense view
        response = self.client.post(reverse('delete_expense', args=[self.expense.id]))
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
            'category': 'Entertainment',
            'amount': 200,
            'date': '2023-12-10'
        }
        response = self.client.post(reverse('create_expense'), data)
        self.assertRedirects(response, reverse('view_expenses'))
        self.assertTrue(Expense.objects.filter(category='Entertainment', amount=200, user=self.user).exists())

    def test_create_expense_post_invalid(self):
        # Test POST request to create expense view with invalid data
        data = {
            'category': '',
            'amount': '',
            'date': ''
        }
        response = self.client.post(reverse('create_expense'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))