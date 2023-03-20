from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission
from rest_framework.views import APIView, Response, status
from datetime import datetime
from rest_framework.serializers import Serializer, CharField, BooleanField, DateField,\
    IntegerField, ModelSerializer
from django.contrib.auth.models import User
from core.services.user import create_user, update_user, delete_user
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from core.shared.permission import UserPermission, UserDataPermission


class CustomAuthToken(ObtainAuthToken):
    """
    Obtain an authentication token for an authenticated user.

    This view allows a user to generate a token to use for
    authenticating with the API.


    **Accepted parameters:**

    - `username`
    - `password`



    """

    def post(self, request, *args, **kwargs):
        """
            This is the endpoint for logging in a user. It returns a token that can be used in
            future requests.

            :param request: The request object that contains the user's email and password.
            :type request: rest_framework.request.Request
            :return: A response object with the token and other user information.
            :rtype: rest_framework.views.Response
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        permissions = None
        if not user.is_superuser:
            permissions = Permission.objects.filter(user=user)
        else:
            permissions = Permission.objects.all()

        perm_tuple = ["{0}.{1}".format(
            x.content_type.app_label, x.codename) for x in permissions]
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'fecha': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            'permissions': perm_tuple,
            'is_superuser': user.is_superuser,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'username': user.username,
            'date_joined': user.date_joined,
            
            
        }, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})


class getAllUser(APIView):
    permission_classes = (IsAuthenticated,
                          )
    permission_required = 'core.view_user'
    model = User

    class UserSerializer(ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_superuser',
                      'is_staff', 'is_active', 'date_joined')

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = self.UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class createUser(APIView):
    permission_classes = [IsAuthenticated, UserPermission]
    model = User
    permission_required = 'core.add_user'

    class UserSerializer(Serializer):
        username = CharField(max_length=100)
        password = CharField(max_length=100)
        email = CharField(max_length=100)

    def post(self, request, format=None):
        serializer = self.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        create_user(user)
        return Response(serializer.data, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})


class updateUser(APIView):
    permission_classes = [IsAuthenticated, UserDataPermission]
    model = User
    permission_required = 'core.change_user'

    class UserSerializer(Serializer):
        username = CharField(max_length=100)
        password = CharField(max_length=100)
        email = CharField(max_length=100)

    def post(self, request, user_id):
        serializer = self.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        update_user(user_id, data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})


class deleteUser(APIView):
    """
    Deletes the user with the given user_id
    """
    permission_classes = [IsAuthenticated, UserPermission]
    model = User
    permission_required: str = 'core.delete_user'

    def post(self, request, user_id) -> Response:
        delete_user(user_id)
        return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})


class logOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})
