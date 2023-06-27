# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import ParametersTestSerializer
# Task model
from .models import ParametersTest


@csrf_exempt

def parametersView(request):
    if request.method == 'GET':
        
        param = ParametersTest.objects.all()
        serializer = ParametersTestSerializer(param, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serializer = ParametersTestSerializer(data=data)

        if serializer.is_valid():
            
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def parametersViewDetail(request, pk):

    try:
        # obtain the Parameters with the passed id.
        param = ParametersTest.objects.get(pk=pk)
        
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = ParametersTestSerializer(param, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the task
        param.delete() 
        # return a no content response.
        return HttpResponse(status=204) 


