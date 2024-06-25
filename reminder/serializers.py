from rest_framework import serializers

from .models import Person, Event


class PersonSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonCreateUpdateSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'birth_date',
            'notification_time',
            'message',
            'send_message_time',
            'congrats_birth',
            'congrats_birth_message',
            'send_type',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
