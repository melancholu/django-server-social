from rest_framework import mixins, viewsets

from apps.feed.models import Feed
from apps.feed.serializers import FeedSerializer


class FeedViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
