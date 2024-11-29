from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'home'),
    path('create_expense', views.create_expense, name = 'create_expense')
]