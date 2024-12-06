from django.contrib import admin
from .models import Expense

# Remove the import for ExpenseCategory as it is no longer needed
# from .models import Expense, ExpenseCategory

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date','amount', 'description', 'category', 'user')
    search_fields = ('description', 'category', 'user__username') # update search fields to use 'category' for conversion from pick list to user input
    list_filter = ('date', 'category', 'user')

# Remove the registration for ExpenseCategory as it is no longer needed
# @admin.register(ExpenseCategory)
# class ExpenseCategoryAdmin(admin.ModelAdmin):
#     list_display = ('expense_type',)
#     search_fields = ('expense_type',)
