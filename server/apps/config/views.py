import json
from django.http import JsonResponse
from .mqtt import client as mqtt_client
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})