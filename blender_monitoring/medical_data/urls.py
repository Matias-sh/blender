from django.urls import path

def test_view(request):
    return JsonResponse({'message': 'Medical data app is working!'})

urlpatterns = [
    path('test/', test_view, name='test_view'),
]
