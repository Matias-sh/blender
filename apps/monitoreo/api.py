from .models import *
from rest_framework import viewsets, permissions
from .serializers import ParametrosPruebaSerializers

class ParametrosViewSet(viewsets.ModelViewSet):
    queryset = ParametrosPrueba.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParametrosPruebaSerializers
