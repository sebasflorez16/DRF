
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

#Maneja el uso de los tokens que viene por defecto en DRF 1° paso
from rest_framework.authtoken.views import ObtainAuthToken 


from apps.users.api.serializers import UserTokenSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context={'request':request}) #El serializador viene contenido en el ObtainAuthToken
        if login_serializer.is_valid():
            user = login_serializer.validate_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user) #Esto lo serializa luego de ser creado
                if created:
                    return Response({

                        'token': token.key,  #Para el user nuevo crea un token
                        'user': user_serializer.data,     #Cuando se crea se debe serializar
                        'message': "Inicio de sesion exitoso"

                    }, status = status.HTTP_201_CREATED)
                else:
                    """
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())#Borra todas las sesiones del usuario segun el tiempo
                    if all_sessions.exist():
                        for session in all_sessions:
                            session_data = session.get_decode()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()

                    token.delete()
                    token = Token.objects.create(user=user)
                    """

                    token.delete()
                    return Response({
                        'error':'Y se inicion sesion con esta cuenta'
                    }, status = status.HTTP_409_CONFLICT)    #bloquea el intent de sesion en dos partes iguales
            else:
                return Response({'error':'Este usuario no puede iniciar seseion'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({'error':'Username o Password son in invalidos'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"mensaje":"Hola desde response"}, status = status.HTTP_200_OK)

#Para el logout se puede hacer la peticion ya sea por GET o por POST
class Logout(APIView):
    def post(self,request, *args, **kwargs):

        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            
            if token:
                user = token.user

                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())#Borra todas las sesiones del usuario segun el tiempo que se le indique
                if all_sessions.exist():
                    for session in all_sessions:
                        session_data = session.get_decode()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()

                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado'
                return Response({'session_message':session_message, 'token_message':token_message},
                                status=status.HTTP_200_OK)
            
            return Response({'error':'No se ha encontrado usuario con esas credenciales'},
                                status = status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error':'No se ha encontrado tokoen'},
                                status = status.HTTP_409_CONFLICT)   
