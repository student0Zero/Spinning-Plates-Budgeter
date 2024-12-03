from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    expense_type = models.CharField(max_length=50)

    def __str__(self):
        return self.expense_type

class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - {self.amount}"