# using django generic class based viewa
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm

# commented out to change approach with login page as default if not auth, otherwise view_expenses.html if user auth
# class Index(TemplateView):
#     template_name = 'home/index.html'

def home(request):
    if request.user.is_authenticated:
        return redirect('view_expenses')
    else:
        return redirect('account_login')

def view_expenses(request):
    # Get all expenses for the logged-in user
    expenses = Expense.objects.filter(user=request.user)
    
    # Aggregate the sum of amounts spent in each category
    category_totals = (
        expenses
        .values('category__expense_type')  # Group by category name
        .annotate(total_spent=Sum('amount'))  # Calculate total amount per category
        .order_by('category__expense_type')  # Optional: Order categories alphabetically
    )
    
    # Prepare data for Chart.js
    labels = [item['category__expense_type'] for item in category_totals]
    data = [float(item['total_spent']) for item in category_totals]  # Convert Decimal to float


    context = {
        "expenses": expenses,  # Still passing expenses if needed elsewhere
        "labels": labels,  # Labels for Chart.js
        "data": data,  # Data for Chart.js
    }

    return render(request, 'home/view_expenses.html', context)

def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            # messages.success(request, "Expense created.")
            return redirect('home')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = ExpenseForm()
        context = {
            "form": form,
        }
        return render(request, 'home/create_expense.html', context)


def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            # messages.success(request, "Expense edited.")
            return redirect('home')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)
        context = {
            "form": form,
        }
        return render(request, 'home/edit_expense.html', context)



def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        expense.delete()
        # messages.success(request, "Expense deleted successfully.")
        return redirect("home")
    else:
        return render(request, 'home/delete_expense.html')