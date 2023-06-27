
from django.urls import path 
from .views import *

urlpatterns = [
    path('parameters/', parametersView),
    path('parameters/<int:pk>/', parametersViewDetail),
]