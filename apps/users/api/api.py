
#Archivos de vistas de la data que se va retornar en formato json
from decimal import Context
from rest_framework import status  #codigos de estado para enviar luego del response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User


@api_view(['GET', 'POST', ])#Especifica cual se va a mostrar en la apiview
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all().values() # Values hace que el serializer devuelva un diccionario si no se pone "TypeError: 'User' object is not subscriptable"
        users_serializer = UserListSerializer(users, many=True) #many=True para que el serializer sepa que son varios objetos como la el query de arriba all()
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    
    #create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)#Si son los mismos campos del modelo podemos enviarle informacion a la data para guardar ese modelo como un nuevo registo pero enviandolo de json al modelo
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)   



@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    #queryset
    user = User.objects.filter(id = pk).first()  #filtra todas las peticiones de los metodos http 1 sola vez la consulta
    if user:

        #Lisr
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        #update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user,data = request.data) # Asi valida para enviar al serializer y actualice
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)#despues de validar devuelve objeto actualizado
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message','Usuario eliminado correctamente!'}, status = status.HTTP_200_OK) #pasar como diccionario cariable 'message' valor 'el mensaje'

    return Response({'message', 'No se encontro ningun usuario'}, status=status.HTTP_400_BAD_REQUEST)