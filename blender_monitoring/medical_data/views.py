from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MonitoringData
from .serializers import MonitoringDataSerializer

class LatestMonitoringDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        patient_id = request.query_params.get('patient_id')
        if not patient_id:
            return Response({'error': 'Patient ID is required'}, status=400)

        latest_data = MonitoringData.objects.filter(patient__id=patient_id).last()
        if latest_data:
            serializer = MonitoringDataSerializer(latest_data)
            return Response(serializer.data)
        return Response({'error': 'No data found'}, status=404)
