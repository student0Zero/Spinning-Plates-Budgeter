from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IncomeCategory(models.Model):
    income_type = models.CharField(max_length=150)

    def __str__(self):
        return self.income_type
    
class Income(models.Model):
    date = models.DateField()
    in_amount = models.DecimalField(max_digits=100, decimal_places=4)
    description = models.TextField()
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='income_app_incomes')

    def __str__(self):
        return f"{self.description} - {self.in_amount}"