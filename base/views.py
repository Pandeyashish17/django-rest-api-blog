from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import article,author,categories,tag
from .serializers import articleSerializer,authorSerializer,categorySerializer,tagSerializer
# Create your views here.



def home(request):
    return HttpResponse("hello")


def articles(request):
    if request.method == "GET":
        articles = article.objects.all()
        serializer=articleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)
            
           



           
       
def singleArticles(request,pk):
    try:
         singleArticle = article.objects.get(pk=pk)
    except article.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == "GET":
        serializer = articleSerializer(singleArticle)
        return JsonResponse(serializer.data)






def authors(request):
    if request.method == "GET":
        authors=author.objects.all()
        serializer=authorSerializer(authors,many=True)
        return JsonResponse(serializer.data,safe=False)

def category(request):
    if request.method == "GET":
        categories=categories.objects.all()
        serializer=categorySerializer(categories,many=True)
        return JsonResponse(serializer.data,safe=False)

def tags(request):
    if request.method == "GET":
        tags=tag.objects.all()
        serializer=tagSerializer(tags,many=True)
        return JsonResponse(serializer.data,safe=False)