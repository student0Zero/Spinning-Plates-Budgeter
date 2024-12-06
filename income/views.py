from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Income
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def income(request):
    if request.user.is_authenticated:
        return redirect('view_income')
    else:
        return redirect('account_login')

# View income
@login_required
def view_income(request):
    # Get all income for the logged-in user
    incomes = Income.objects.filter(user=request.user)

    # Aggregate the sum of amounts earned in each category
    income_by_category = (
        incomes
        .values('category')  # Group by category name (updated to use CharField)
        .annotate(total_amount=Sum('in_amount'))  # Calculate total amount per category
        .order_by('category')  # Optional: Order categories alphabetically
    )

    # Prepare data for Chart.js
    labels = [item['category'] for item in income_by_category]  # Updated to use CharField
    data = [float(item['total_amount']) for item in income_by_category]  # Convert Decimal to float

    context = {
        "incomes": incomes,  # Pass the incomes to the template
        'income_by_category': income_by_category,  # Pass the income by category to the template
        "labels": labels,  # Labels for Chart.js
        "data": data,  # Data for Chart.js
    }

    return render(request, 'income/view_income.html', context)

# Create income
@login_required
def create_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user  # Assign the logged-in user
            income.save()
            return redirect('view_income')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = IncomeForm()
        context = {
            "form": form,
        }
        return render(request, 'income/create_income.html', {'form': form})

# Edit income
@login_required
def edit_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            # messages.success(request, "Income edited.")
            return redirect('view_income')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = IncomeForm(instance=income)
        context = {
            "form": form,
        }
        return render(request, 'income/edit_income.html', context)

# Delete income
@login_required
def delete_income(request, id):
    income = get_object_or_404(Income, id=id)
    if request.method == "POST":
        income.delete()
        # messages.success(request, "Income deleted successfully.")
        return redirect("view_income")
    else:
        return render(request, 'income/delete_income.html')