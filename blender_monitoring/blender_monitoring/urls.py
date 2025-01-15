from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin
    path('dashboard/', include('dashboard.urls')),  # Rutas de la app Dashboard
    path('api/users/', include('users.urls')),  # Rutas de la app Users
    path('api/patients/', include('patients.urls')),  # Rutas de la app Patients
    path('api/medical_data/', include('medical_data.urls')),  # Rutas de la app Medical Data
]
