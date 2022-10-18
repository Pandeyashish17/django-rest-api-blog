from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import article,author
from .serializers import articleSerializer,authorSerializer
# Create your views here.



def home(request):
    return HttpResponse("hello")


def articles(request):
    if request.method == "GET":
        articles=article.objects.all()
        serializer=articleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)


def authors(request):
    if request.method == "GET":
        authors=author.objects.all()
        serializer=authorSerializer(authors,many=True)
        return JsonResponse(serializer.data,safe=False)