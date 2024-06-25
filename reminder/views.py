from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from account.models import Profile
from .models import Person
from . import serializers


class PersonView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = get_object_or_404(Profile, user_rel=request.user)
        persons = Person.objects.filter(person_profile_rel=profile)
        if persons.exists():
            serializer = serializers.PersonSerailizers(instance=persons, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={"message": "Persons not exists"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        profile = get_object_or_404(Profile, user_rel=request.user)
        serializer = serializers.PersonCreateSerailizers(data=request.data)
        if serializer.is_valid():
            person = Person(person_profile_rel=profile, **serializer.validated_data)
            person.save()
            return Response(data={"message": "Create person sucsessfuly"}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
