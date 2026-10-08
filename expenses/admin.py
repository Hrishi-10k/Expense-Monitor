from django.contrib import admin

from .models import Budget, Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user']
    search_fields = ['name', 'user__username']
    list_filter = ['user']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'category', 'amount', 'expense_date', 'created_at']
    search_fields = ['description', 'category__name', 'user__username']
    list_filter = ['category', 'expense_date', 'user']
    list_select_related = ['user', 'category']


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'category', 'monthly_limit']
    search_fields = ['category__name', 'user__username']
    list_filter = ['category', 'user']
    list_select_related = ['user', 'category']
