from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from expenses.models import Expense
from income.models import Income
from django.utils.dateformat import DateFormat
from django.contrib.auth.decorators import login_required


# landing page view
def index(request):
    return render(request, 'home/index.html')


@login_required
def home_view(request):
    expenses = Expense.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)

    # Aggregate the sum of amounts spent in each month
    monthly_expense_summary = (
        expenses.annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total_amount=Sum("amount"))
        .order_by("month")
    )
    monthly_income_summary = (
        incomes.annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total_amount=Sum("in_amount"))
        .order_by("month")
    )

    # Aggregate the sum of amounts spent in each category
    expense_summary = (
        expenses.values("category")
        .annotate(total_amount=Sum("amount"))
        .order_by("category")
    )
    income_summary = (
        incomes.values("category")
        .annotate(total_amount=Sum("in_amount"))
        .order_by("category")
    )

    # Calculate the sum of all expenses and income for the logged-in user
    total_expenses = expenses.aggregate(Sum("amount"))["amount__sum"] or 0
    total_income = incomes.aggregate(Sum("in_amount"))["in_amount__sum"] or 0

    # Calculate the percentage of total expenses relative to total income
    if total_income > 0:
        expense_percentage = (total_expenses / total_income) * 100
    else:
        expense_percentage = 0

    # Prepare data for Chart.js
    expense_labels = [
        DateFormat(item["month"]).format("Y-m")
        for item in monthly_expense_summary
    ]
    expense_data = [
        float(item["total_amount"])
        for item in monthly_expense_summary]
    income_labels = [
        DateFormat(item["month"]).format("Y-m")
        for item in monthly_income_summary
    ]
    income_data = [
        float(item["total_amount"])
        for item in monthly_income_summary]

    context = {
        "expenses": expenses,
        "incomes": incomes,
        "expense_summary": expense_summary,
        "income_summary": income_summary,
        "total_expenses": total_expenses,
        "total_income": total_income,
        "expense_percentage": expense_percentage,
        "expense_labels": expense_labels,
        "expense_data": expense_data,
        "income_labels": income_labels,
        "income_data": income_data,
    }
    return render(request, "home/home.html", context)
