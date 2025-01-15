from django.urls import path

def test_view(request):
    return JsonResponse({'message': 'Patients app is working!'})

urlpatterns = [
    path('test/', test_view, name='test_view'),
]
