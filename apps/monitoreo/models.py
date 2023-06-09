from django.db import models

# Create your models here.

class ParametrosPrueba(models.Model):
    id_parametro = models.AutoField(primary_key=True)
    dato1 = models.CharField(max_length=50)
    dato2 = models.CharField(max_length=50)
    dato3 = models.CharField(max_length=50)
    dato4 = models.CharField(max_length=50)

