from django.shortcuts import render
from django.db.models import Sum
from expenses.models import Expense
from income.models import Income
from django.utils.dateformat import DateFormat
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth

@login_required
def home_view(request):
    expenses = Expense.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)

    # Aggregate by month
    expense_summary = expenses.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('amount')).order_by('month')
    income_summary = incomes.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('in_amount')).order_by('month')

    # Calculate the sum of all expenses and income for the logged-in user
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = incomes.aggregate(Sum('in_amount'))['in_amount__sum'] or 0

    # Prepare data for Chart.js
    # Convert the date to a string for home.html view
    expense_labels = [DateFormat(item['month']).format('Y-m') for item in expense_summary]
    expense_data = [float(item['total_amount']) for item in expense_summary]
    # Convert the date to a string for home.html view
    income_labels = [DateFormat(item['month']).format('Y-m') for item in income_summary]
    income_data = [float(item['total_amount']) for item in income_summary]

    context = {
        'expenses': expenses,
        'incomes': incomes,
        'expense_summary': expense_summary,
        'income_summary': income_summary,
        'total_expenses': total_expenses,
        'total_income': total_income,
        'expense_labels': expense_labels,
        'expense_data': expense_data,
        'income_labels': income_labels,
        'income_data': income_data,
    }
    return render(request, 'home/home.html', context)