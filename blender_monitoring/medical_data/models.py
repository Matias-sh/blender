from django.db import models
from patients.models import Patient

class MonitoringData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="monitoring_data")
    oxygen = models.FloatField()
    pressure = models.FloatField()
    flow = models.FloatField()
    co2 = models.FloatField()
    spo2 = models.FloatField()
    alarm = models.BooleanField(default=False)

    def __str__(self):
        return f"Data for {self.patient.name} at {self.timestamp}"

class AlarmLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="alarm_logs")

    def __str__(self):
        return f"Alarm for {self.patient.name} at {self.timestamp}"
