from rest_framework import serializers
from .models import MonitoringData, AlarmLog

class MonitoringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringData
        fields = '__all__'

class AlarmLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmLog
        fields = '__all__'
