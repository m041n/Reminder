from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from account.models import Profile
from .models import Person, Event
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
        serializer = serializers.PersonCreateUpdateSerailizers(data=request.data)
        if serializer.is_valid():
            person = Person(person_profile_rel=profile, **serializer.validated_data)
            person.save()
            return Response(data={"message": "Create person sucsessfuly"}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonUpdateDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        serializer = serializers.PersonCreateUpdateSerailizers(instance=person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Update person successfully"}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        person.delete()
        return Response(data={"message": "Deleted successfully"}, status=status.HTTP_200_OK)


class EventView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = get_object_or_404(Profile, user_rel=request.user)
        event = Event.objects.filter(person_profile_rel=profile)
        if event.exists():
            serializer = serializers.EventSerializer(instance=event, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={"message": "Event doesn't exists"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        profile = get_object_or_404(Profile, user_rel=request.user)
        serializer = serializers.EventCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            persons = serializer.validated_data.pop("persons_rel")
            event = Event(person_profile_rel=profile, **serializer.validated_data)
            event.save()
            event.persons_rel.add(*persons)
            return Response(data={"message": "Create event sucsessfuly"}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)