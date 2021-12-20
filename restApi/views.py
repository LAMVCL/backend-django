from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from restApi.models import RestApi
from restApi.serializers import RestApiSerializer

# Create your views here.
@csrf_exempt
def todo_detail(request,id = 0):
    #Si el metodo de la petición es get entonces se ejecuta el codigo
    if request.method == 'GET':
        #Asignamos al todo los objetos que se encuentran en la bd
        todo = RestApi.objects.all()
        serializer = RestApiSerializer(todo, many=True)
        return JsonResponse(serializer.data, safe=False)
    #Si el metodo de la peticion es POST entonces insertamos una nueva tarea
    elif request.method == 'POST':
        #Parseamos la solicitud y la asignamos a data
        data_todo = JSONParser().parse(request)
        #Luego mediante el serializer lo convertimos al modelo
        serializer = RestApiSerializer(data=data_todo)
        #Si el modelo es valido entonces lo guardamos mediante save
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        #Si no es valido entonces retornamos un error
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        #Parseamos la solicitud y la asignamos a data
        data_todo = JSONParser().parse(request)
        todo = RestApi.objects.get(id=data_todo['id'])
        serializer = RestApiSerializer(todo, data=data_todo)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        try:
            todo = RestApi.objects.get(id=id)
            todo.delete()
            return HttpResponse(status=200);
        except:
            return HttpResponse(status=400);
        