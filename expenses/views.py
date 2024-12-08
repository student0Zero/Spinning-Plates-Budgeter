from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm
from income.models import Income
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth
from django.utils.dateformat import DateFormat

@login_required
def view_expenses(request):
    # Get all expenses for the logged-in user
    expenses = Expense.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)

    # Aggregate the sum of amounts spent in each category
    category_totals = (
        expenses
        .values('category')  # Group by category name
        .annotate(total_spent=Sum('amount'))  # Calculate total amount per category
        .order_by('category')  # Optional: Order categories alphabetically
    )

    # Aggregate the sum of amounts spent in each month
    monthly_expense_summary = expenses.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('amount')).order_by('month')
    monthly_income_summary = incomes.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('in_amount')).order_by('month')


    # Calculate the sum of all expenses and income for the logged-in user
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = incomes.aggregate(Sum('in_amount'))['in_amount__sum'] or 0

    # Calculate the percentage of total expenses relative to total income
    if total_income > 0:
        expense_percentage = (total_expenses / total_income) * 100
    else:
        expense_percentage = 0

    # Prepare data for Chart.js
    expense_labels = [DateFormat(item['month']).format('Y-m') for item in monthly_expense_summary]
    expense_data = [float(item['total_amount']) for item in monthly_expense_summary]

    # labels = [item['category'] for item in category_totals]
    # data = [float(item['total_spent']) for item in category_totals]

    # Query to get the sum of expenses for each category
    expenses_by_category = expenses.values('category').annotate(total_amount=Sum('amount')).order_by('-total_amount')

    context = {
        "expenses": expenses,
        'expense_summary': category_totals,
        'expense_by_category': expenses_by_category,  # Corrected variable name
        'expense_percentage': expense_percentage,
        'total_expenses': total_expenses,
        'total_income': total_income,
        "expense_labels": expense_labels,
        "expense_data": expense_data,
    }
    return render(request, 'expenses/view_expenses.html', context)

@login_required
def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('view_expenses')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = ExpenseForm()
        context = {
            "form": form,
        }
    return render(request, 'expenses/create_expense.html', context)

@login_required
def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('view_expenses')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)
        context = {
            "form": form,
        }

    return render(request, 'expenses/edit_expense.html', context)

@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        expense.delete()
        return redirect("view_expenses")
    else:
        return render(request, 'expenses/delete_expense.html')