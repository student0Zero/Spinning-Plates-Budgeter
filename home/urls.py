from django.urls import path
from .views import home_view
from . import views as views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path('summary', home_view, name="home"),
]
