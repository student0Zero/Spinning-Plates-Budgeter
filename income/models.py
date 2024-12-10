from django.db import models
from django.contrib.auth.models import User


class IncomeCategory(models.Model):
    income_type = models.CharField(max_length=150)

    def __str__(self):
        return self.income_type


class Income(models.Model):
    date = models.DateField()
    in_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(
        max_length=100
    )  # Change to CharField to allow custom input
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="income_app_incomes"
    )

    def __str__(self):
        return f"{self.description} - {self.in_amount}"
