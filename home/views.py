# using django generic class based viewa
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import ExpenseForm


class Index(TemplateView):
    template_name = 'home/index.html'


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