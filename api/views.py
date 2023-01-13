from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerialize

# Create your views here.
# @csrf_exempt

@api_view(["GET", "POST"])
def article_list(request):
    #get all articles
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerialize(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerialize(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# def article_list(request):

#     #get all articles
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerialize(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerialize(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ArticleSerialize(article)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerialize(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)

# class ArticleView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialize
