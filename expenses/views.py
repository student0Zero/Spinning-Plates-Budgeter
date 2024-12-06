# using django generic class based view
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

# commented out to change approach with login page as default if not auth, otherwise view_expenses.html if user auth
# class Index(TemplateView):
#     template_name = 'home/index.html'

@login_required
def expenses(request):
    if request.user.is_authenticated:
        return redirect('view_expenses')
    else:
        return redirect('account_login')

@login_required
def view_expenses(request):
    # Get all expenses for the logged-in user
    expenses = Expense.objects.filter(user = request.user)
    
    # Aggregate the sum of amounts spent in each category
    category_totals = (
        expenses
        .values('category')  # Group by category name (updated to use Charfield to allow for user defined categories)
        .annotate(total_spent = Sum('amount'))  # Calculate total amount per category
        .order_by('category')  # Optional: Order categories alphabetically (updated to use Charfield to allow for user defined categories)
    )
    
    # Prepare data for Chart.js
    labels = [item['category'] for item in category_totals] # (updated to use Charfield to allow for user defined categories)
    data = [float(item['total_spent']) for item in category_totals]  # Convert Decimal to float. 

    # Query to get the sum of expenses for each category
    # (updated to use Charfield to allow for user defined categories)
    expenses_by_category = Expense.objects.filter(user=request.user).values('category').annotate(total_amount=Sum('amount')).order_by('-total_amount')

    context = {
        "expenses": expenses,  # Still passing expenses if needed elsewhere
        'expenses_by_category': expenses_by_category,  # Pass the expenses by category to dataTable in view_expenses.html
        "labels": labels,  # Labels for Chart.js
        "data": data,  # Data for Chart.js
    }

    return render(request, 'expenses/view_expenses.html', context)

@login_required
def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit = False)
            expense.user = request.user
            expense.save()
            #messages.success(request, "Expense created.")
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
        form = ExpenseForm(request.POST, instance = expense)
        if form.is_valid():
            expense = form.save(commit = False)
            expense.user = request.user
            expense.save()
            #messages.success(request, "Expense edited.")
            return redirect('view_expenses')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = ExpenseForm(instance = expense)
        context = {
            "form": form,
        }

    return render(request, 'expenses/edit_expense.html', context)


##################### delete expense
@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        expense.delete()
        #messages.success(request, "Expense deleted successfully.")
        return redirect("view_expenses")
    else:
        return render(request, 'expenses/delete_expense.html')