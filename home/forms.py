from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'description', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }