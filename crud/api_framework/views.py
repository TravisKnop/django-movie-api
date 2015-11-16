from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from movie.models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = MovieSerializer


class MovieListView(ListCreateAPIView):
    permission_classes = IsAuthenticated
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all
    serializer_class = MovieSerializer
