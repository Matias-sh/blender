from django.db import models
from users.models import User

class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    sex = models.CharField(max_length=10)
    assigned_doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'doctor'})

    def __str__(self):
        return f"{self.name} {self.surname}"
