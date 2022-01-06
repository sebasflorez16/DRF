#Se va a colocar un tiempo de caducidad para el token

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from datetime import timedelta
from django.utils import timezone
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):
#Del codigo fuente del framework

    #Calcula el tiempo de expiracion del token
    def expired_in(self, token):
        time_elapsed = timezone.now() - token.created #Calcula la hora actual con la hora de creacion del token
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed


    #Calcula y confirma si el token ha expirado
    def is_token_expire(self, token):
        return self.expired_in(token) < timedelta( seconds = 0)


    #Obtiene el valor de las funciones anteriores de que si ha expirado el token
    def token_expired_handler(self, token):
        is_expired = self.is_token_expired(token)
        
        if is_expired:
            print("Token expirado.")

            return is_expired


    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key = key)#El get_model() ahorra la importacion de modelo token. devuelve el modelo si es None. Viende dentro del codigo de DRF

        except self.get_model().DoesNotExist:
             raise AuthenticationFailed('Token Invalido.')

        if not token.user.is_active:
            raise AuthenticationFailed('Usuario inactivo o eliminado.')


        #Se llama la variable para que ejecute el calculo
        is_expire = self.token_expired_handler(token)

        if is_expire:
            raise AuthenticationFailed("Su token ha expirado")
        
        return (token.user, token)