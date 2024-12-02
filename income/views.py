from django.shortcuts import render, redirect, get_object_or_404
from .models import Income, IncomeCategory
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# View income
@login_required
def view_income(request):
    incomes_by_category = Income.objects.values('category__income_type').annotate(total_amount=Sum('in_amount'))
    incomes = Income.objects.filter(user=request.user)
    context = {
        'incomes_by_category': incomes_by_category,
        'incomes': incomes,
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