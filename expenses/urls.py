from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('view-expenses/',views.view_expenses,name='view_expenses'),
    path('update-expense/<int:id>/',views.update_expense,name='update_expense'),
    path('delete-expense/<int:id>/',views.delete_expense,name='delete_expense'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add-budget/', views.add_budget, name='add_budget'),
    path('view-budgets/', views.view_budgets, name='view_budgets'),
    path('edit-budget/<int:id>/', views.edit_budget, name='edit_budget'),
    path('delete-budget/<int:id>/', views.delete_budget, name='delete_budget'),
    path('budget-report/',views.budget_report,name='budget_report'),
    path('categories/', views.view_categories, name='view_categories'),
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
    path('export-excel/', views.export_excel, name='export_excel'),
]