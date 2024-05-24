from django.urls import include, path
from rest_framework import routers

from blog.views import MovieViewSet

router = routers.DefaultRouter()

router.register(r'movies', MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]