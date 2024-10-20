from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import CustomTokenObtainPairSerializer, LoginUserSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions,status, exceptions
from django.contrib.auth import authenticate
class LoginUserApi(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    
    get_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_204_NO_CONTENT: 'NO_CONTENT',
        status.HTTP_200_OK: 'JSON',
    }
    post_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_304_NOT_MODIFIED: 'NOT_MODIFIED',
        status.HTTP_200_OK: 'JSON',
    }
    put_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_304_NOT_MODIFIED: 'NOT_MODIFIED',
        status.HTTP_200_OK: 'JSON',
    }
    delete_list_test_response = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: 'INTERNAL_SERVER_ERROR',
        status.HTTP_304_NOT_MODIFIED: 'NOT_MODIFIED',
        status.HTTP_200_OK: 'JSON',
    }
    
    @action(methods=["POST"], detail=False, url_path="login")
    def login(self, request):  
        print("start login")
        print(request.data)
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise exceptions.AuthenticationFailed("Thông tin đăng nhập không chính xác!")
        refresh = CustomTokenObtainPairSerializer.get_token(user)
        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
            , status=status.HTTP_200_OK
            )
        
    @action(methods=["POST"], detail=False, url_path="register")
    def register(self, request):
        serializer =  UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()  # save user to database  
        return Response(
          "success"
            , status=status.HTTP_200_OK
            )