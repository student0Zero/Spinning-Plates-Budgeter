from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    category = forms.CharField(
        max_length=100, label="Category"
    )  # Change to CharField to allow custom input

    # form for creating a new expense
    class Meta:
        model = Expense
        fields = ["date", "amount", "description", "category"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(
                attrs={"rows": 3, "cols": 40}
            ),  # Customize the size of the description field
        }

    # Custom clean method to ensure the amount is negative for expenses.
    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount > 0:
            amount = -amount  # Convert to negative
        elif amount == 0:
            raise forms.ValidationError("The amount must be a negative number.")
        return amount
