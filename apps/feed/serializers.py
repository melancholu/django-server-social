from django.db import IntegrityError

from rest_framework import serializers
from rest_framework.exceptions import ParseError
from rest_framework.relations import SlugRelatedField
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.feed.models import Feed
from apps.user.models import User


class FeedSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field="uuid",
        queryset=User.objects.all(),
        write_only=True,
    )
    content = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Feed
        fields = [
            "user",
            "content",
            "created",
        ]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            print(e)
            raise ParseError(detail="feed already exists", code=HTTP_400_BAD_REQUEST)
