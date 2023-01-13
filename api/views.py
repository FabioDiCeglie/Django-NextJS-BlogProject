from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerialize

# Create your views here.
class ArticleView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialize
