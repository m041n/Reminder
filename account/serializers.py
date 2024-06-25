from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    national_id = serializers.CharField()
    image = serializers.ImageField()
    birth_date = serializers.DateField()
    token = serializers.CharField()

    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        if data['password'] and data['confirm_password'] and data['password'] != data['confirm_password']:
            raise serializers.ValidationError("password must be match")
        data.pop('confirm_password')
        return data