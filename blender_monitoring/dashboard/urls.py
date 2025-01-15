from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('get_latest_data/', views.get_latest_data, name='get_latest_data'),
]
