from django.contrib import admin
from .models import Income, IncomeCategory

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'in_amount', 'description', 'category', 'user')
    search_fields = ('description', 'category__income_type', 'user__username')
    list_filter = ('date', 'category', 'user')

@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('income_type',)
    search_fields = ('income_type',)