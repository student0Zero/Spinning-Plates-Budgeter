# using django generic class based viewa
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm


class Index(TemplateView):
    template_name = 'home/index.html'


def view_expenses(request):
    expenses = Expense.objects.filter(user=request.user)

    context = {
        "expenses": expenses,
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