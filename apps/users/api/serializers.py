
#########################################################
##  Archivo donde vamos a manejar los serializadores  ##
########################################################

from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from apps.users.models import User



#Recibe la peticion de la vista para un usuario nuevo
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username', 'email', 'name', 'last_name')



#Esto es un serializador basado en eun mmodelo
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        return user


class UserListSerializer(serializers.ModelSerializer):
    Model = User

    def to_representation(self, instance):
        #super().to_representation(instance)
        #print(instance)
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email']
        }




"""# Es la secuencia de validaciones que hace un serializador segun la data de la instancia
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()


    def validate_name(self,value):
        #custom validation
        if 'sebastian' in value:
            raise serializers.ValidationError('Error con ese nombre')
        return value



    def validate_email(self,value):
        if value == '':
            raise serializers.ValidationError('indique un email valido')
        
        return value


    def valiate(self,data):
        return data



#creacion o create desde el serializer. recibe despues del .save()

    def create(self, validated_data):
        return User.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance"""


    