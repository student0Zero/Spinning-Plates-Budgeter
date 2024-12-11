from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("date", "amount", "description", "category", "user")
    search_fields = (
        "description",
        "category",
        "user__username",
    )
    list_filter = ("date", "category", "user")
