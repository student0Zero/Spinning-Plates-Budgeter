from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Income, IncomeCategory
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def income(request):
    if request.user.is_authenticated:
        return redirect('view_expenses')
    else:
        return redirect('account_login')

# View income
@login_required
def view_income(request):
    # Get all expenses for the logged-in user
    income = Income.objects.filter(user=request.user)
    
    # Aggregate the sum of amounts spent in each category
    category_totals = (
        income
        .values('category__income_type')  # Group by category name
        .annotate(total_earned=Sum('in_amount'))  # Calculate total amount per category
        .order_by('category__income_type')  # Optional: Order categories alphabetically
    )
    
    # Prepare data for Chart.js
    labels = [item['category__income_type'] for item in category_totals]
    data = [float(item['total_earned']) for item in category_totals]  # Convert Decimal to float

    # Query to get the sum of expenses for each category
    income_by_category = Income.objects.filter(user=request.user).values('category__income_type').annotate(total_amount=Sum('in_amount')).order_by('-total_amount')
    

    context = {
        "income": income,  # Still passing income if needed elsewhere
        'income_by_category': income_by_category,  # Pass the income by category to dataTable in view_income.html
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