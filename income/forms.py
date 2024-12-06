from django import forms
from .models import Income

# removed the original incomeform class definition as part of the upgrade to user inputted categories
# class IncomeForm(forms.ModelForm):
#     class Meta:
#         model = Income
#         fields = ['date', 'in_amount', 'description', 'category']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#         }\

# class for creating custom category input
class IncomeForm(forms.ModelForm):
    category = forms.CharField(max_length = 100, label = 'Category') # change to CharField to allow for user inputted categories

    class Meta:
        model = Income
        fields = ['date', 'in_amount', 'description', 'category'] # to ensure 'in_amount' is used instead of 'amount' which belongs to expenses
        widgets = {
            'date': forms.DateInput(attrs = {'type': 'date'}),
            'description': forms.Textarea(attrs = {'rows': 3, 'cols': 40}), # customize the size of the description field from here
        }
