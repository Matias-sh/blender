from django.shortcuts import render
from django.http import JsonResponse
from .models import MonitoringData

def dashboard_view(request):
    latest_data = MonitoringData.objects.last()
    context = {
        'latest_data': latest_data,
    }
    return render(request, 'dashboard/dashboard.html', context)


def get_latest_data(request):
    latest_data = MonitoringData.objects.last()
    if latest_data:
        data = {
            'oxygen': latest_data.oxygen,
            'pressure': latest_data.pressure,
            'flow': latest_data.flow,
            'co2': latest_data.co2,
            'spo2': latest_data.spo2,
            'alarm': latest_data.alarm
        }
    else:
        data = {}
    return JsonResponse(data)

