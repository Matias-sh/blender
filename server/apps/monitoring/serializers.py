from rest_framework import serializers
from .models import *

class ParametersTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParametersTest

        fields = '__all__'