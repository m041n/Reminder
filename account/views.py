from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Profile
from . import serializers


class RegisterView(APIView):

    def post(self, request):
        user_serializer = serializers.RegisterSerializer(data=request.data)
        if user_serializer.is_valid():
            try:
                with transaction.atomic():
                    user = User(
                        phone_number=user_serializer.validated_data.pop('phone_number'),
                        password=user_serializer.validated_data['password'])
                    user.set_password(user_serializer.validated_data.pop('password'))
                    user.save()
                    user_profile = Profile(user_rel=user, **user_serializer.validated_data)
                    user_profile.save()
                    return Response(data={"message": "You created registered successfully"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response(data={"message": "This user already exist"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
