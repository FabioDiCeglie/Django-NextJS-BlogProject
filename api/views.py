from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerialize

# Create your views here.

def article_list(request):

    #get all articles
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerialize(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# class ArticleView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialize
