from rest_framework import serializers
from .models import *

class ParametrosPruebaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParametrosPrueba

        fields = '__all__'