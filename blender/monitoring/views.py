from django.shortcuts import render
from .models import MonitoringData, AlarmLog

def monitoring_view(request):
    monitoring_data = MonitoringData.objects.all().order_by('-timestamp')[:10]
    alarm_logs = AlarmLog.objects.all().order_by('-timestamp')[:10]
    context = {
        'monitoring_data': monitoring_data,
        'alarm_logs': alarm_logs,
    }
    return render(request, 'monitoring.html', context)
