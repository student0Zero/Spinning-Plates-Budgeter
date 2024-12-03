from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('view_income/', views.view_income, name='view_income'),
    path('create_income/', views.create_income, name='create_income'),
    path('edit_income/<int:id>/', views.edit_income, name='edit_income'),
    path('delete_income/<int:id>/', views.delete_income, name='delete_income'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
]