from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.authenticationServices.models import User
class UserSerializer(ModelSerializer):
    class Meta: 
        model = User
        fields = ["id","username","password","email", "is_active"]
        extra_kwargs = {
            'password' : { 'write_only' : True }
                }
    def create(self,validated_data) :
        password = validated_data.pop('password', None)
        instance = self.Meta.model ( ** validated_data )
        if password is not None :
            instance.set_password( password )
        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True) 
    password = serializers.CharField(write_only=True)