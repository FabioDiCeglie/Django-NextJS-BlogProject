from django.urls import path
from .views import  ArticleView

urlpatterns = [
    path("article", ArticleView.as_view())
]
