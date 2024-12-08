from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def view_expenses(request):
    # Get all expenses for the logged-in user
    expenses = Expense.objects.filter(user=request.user)

    # Aggregate the sum of amounts spent in each category
    category_totals = (
        expenses
        .values('category')  # Group by category name
        .annotate(total_spent=Sum('amount'))  # Calculate total amount per category
        .order_by('category')  # Optional: Order categories alphabetically
    )

    # Prepare data for Chart.js
    labels = [item['category'] for item in category_totals]
    data = [float(item['total_spent']) for item in category_totals]

    # Query to get the sum of expenses for each category
    expenses_by_category = expenses.values('category').annotate(total_amount=Sum('amount')).order_by('-total_amount')

    context = {
        "expenses": expenses,
        'expense_by_category': expenses_by_category,  # Corrected variable name
        "labels": labels,
        "data": data,
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