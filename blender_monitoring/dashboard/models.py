from django.db import models

class MonitoringData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    oxygen = models.FloatField()
    pressure = models.FloatField()
    flow = models.FloatField()
    co2 = models.FloatField()
    spo2 = models.FloatField()
    alarm = models.BooleanField(default=False)
    #id_paciente
    
    def __str__(self):
        return f"Data: {self.timestamp}"

#class Paciente(models.model):
    #id_paciente
    #nombre
    #apellido
    #peso
    #altura
    #sexo

    

class AlarmLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"Alarm: {self.timestamp}"

class SensorReading():
    timestamp = models.DateTimeField(auto_now_add=True)
    ph_value = models.FloatField()

    def __str__(self):
        return f"{self.ph_value} at {self.timestamp}"