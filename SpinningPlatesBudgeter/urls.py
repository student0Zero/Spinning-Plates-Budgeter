from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('income/', include('income.urls')),  # Include the income app URLs
    path('', include('home.urls')),  # Include the home app URLs
    path('accounts/', include('allauth.urls')),  # Include the allauth URLs
]