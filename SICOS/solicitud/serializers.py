from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    area = serializers.CharField()
    cargo = serializers.CharField()


    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.password = set_password(validated_data.get('password'))
        instance.area = validated_data.get('area')
        instance.cargo = validated_data.get('cargo')
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(data) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, por favor Ingrese uno nuevo")
        else:
            return data

