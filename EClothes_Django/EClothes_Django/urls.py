from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
]
# Djoser provides DRF views to handle basic actions such as 
# registration, login, logout, account auth etc
