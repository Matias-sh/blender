from .models import *
from rest_framework import viewsets, permissions
from .serializers import ParametersTestSerializer

class ParametersViewSet(viewsets.ModelViewSet):
    queryset = ParametersTest.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParametersTestSerializer
