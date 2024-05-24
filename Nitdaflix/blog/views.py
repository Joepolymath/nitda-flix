from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from blog.models import Movie
from blog.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

