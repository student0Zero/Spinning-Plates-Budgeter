from django import forms
from . models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        fields = ['date', 'in_amount', 'description', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }