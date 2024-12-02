from django.urls import path
from . import views

urlpatterns = [
    path('create_income/', views.create_income, name='create_income'),
    path('edit_income/<int:id>/', views.edit_income, name='edit_income'),
    path('delete_income/<int:id>/', views.delete_income, name='delete_income'),
    path('view_income/', views.view_income, name='view_income'),
]