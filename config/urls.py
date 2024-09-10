from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from apps.feed.viewsets import FeedViewSet
from apps.user.viewsets import UserViewSet

router = DefaultRouter()
router.register("feed", FeedViewSet)
router.register("user", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
