from django.urls import path

# Placeholder view para prueba
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({'message': 'Users app is working!'})

urlpatterns = [
    path('test/', test_view, name='test_view'),
]
