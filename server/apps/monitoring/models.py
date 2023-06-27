from django.db import models

# Create your models here.

class ParametersTest(models.Model):
    id_param = models.AutoField(primary_key=True)
    data1 = models.CharField(max_length=50)
    data2 = models.CharField(max_length=50)
    data3 = models.CharField(max_length=50)
    data4 = models.CharField(max_length=50)

