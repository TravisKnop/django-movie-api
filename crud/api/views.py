from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from movie.models import Movie


@csrf_exempt
def api_movie_list_view(request):
    if request.method == "GET":
        qs = Movie.objects.all()
        return HttpResponse(serializers.serialize("json", qs), content_type = "application/json")
    elif request.method == "POST":
        data = request.POST
        new_movie = Movie.objects.create(title=data['title'])
        return HttpResponse(serializers.serialize("json", [movie]), status=201, content_type="application/json")

@csrf_exempt
def api_movie_detail_view(request, model_pk):
    if request.method == "POST":
        return HttpResponse("[]", status=409, content_type="application/json")