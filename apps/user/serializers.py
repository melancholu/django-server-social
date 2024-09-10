from django.db import IntegrityError

from rest_framework import serializers
from rest_framework.exceptions import ParseError
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    image_url = serializers.CharField(required=False)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = [
            "uuid",
            "name",
            "email",
            "password",
            "image_url",
            "created",
        ]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            raise ParseError(detail="user already exists", code=HTTP_400_BAD_REQUEST)
