from django.urls import path,include
# from .views import  ArticleList, ArticleDetails
from .views import ArticleViewSet, UserViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter
# article_list, article_details

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("articles", ArticleList.as_view()),
    # path("articles/<int:id>/", ArticleDetails.as_view())
]
