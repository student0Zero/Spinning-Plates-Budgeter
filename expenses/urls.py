from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("view_expenses", views.view_expenses, name="view_expenses"),
    path("create_expense", views.create_expense, name="create_expense"),
    path("edit_expense/<id>", views.edit_expense, name="edit_expense"),
    path("delete_expense/<id>", views.delete_expense, name="delete_expense"),
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="account_login",
    ),
]
