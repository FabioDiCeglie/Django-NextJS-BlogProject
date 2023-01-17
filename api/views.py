from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerialize

# Create your views here.


class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialize


# -------------------------------------------------------------------

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self,request):
#         articles = Article.objects.all()
#         serializer = ArticleSerialize(articles, many=True)
#         return Response(serializer.data)

#     def create(self,request):
#         serializer = ArticleSerialize(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self,request,pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerialize(article)
#         return Response(serializer.data)

#     def update(self,request,pk=None):
#         article = Article.objects.get(pk=pk)

#         serializer = ArticleSerialize(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self,request,pk=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# -------------------------------------------------------------------

# class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialize
#     def get(self,request):
#         return self.list(request)

#     def post(self,request):
#         return self.create(request)

# class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialize
#     lookup_field = 'id'

#     def get(self,request,id):
#         return self.retrieve(request, id=id)

#     def put(self,request,id):
#         return self.update(request,id=id)

#     def delete(self,request,id):
#         return self.destroy(request,id=id)


# -------------------------------------------------------

# class ArticleList(APIView):
#     def get(self,request):
#         articles = Article.objects.all()
#         serializer = ArticleSerialize(articles, many=True)
#         return Response(serializer.data)

#     def post (self, request):
#         serializer = ArticleSerialize(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):

    # def get_object(self,id):
    #     print(id)
    #     try:
    #         return Article.objects.get(id=id)

    #     except Article.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def get(self,request, id):
    #     article = self.get_object(id)
    #     serializer = ArticleSerialize(article)
    #     return Response(serializer.data)

    # def put(self,request,id):
    #     article = self.get_object(id)
    #     serializer = ArticleSerialize(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request,id):
    #     article = self.get_object(id)
    #     article.delete()
    #     return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# -------------------------------------------------------

# @api_view(["GET", "POST"])
# def article_list(request):
#     #get all articles
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleSerialize(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerialize(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerialize(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerialize(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------

# @csrf_exempt
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


