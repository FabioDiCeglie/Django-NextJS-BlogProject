import graphene
from graphene_django import DjangoObjectType

from .models import Article

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ["id", "title","coverImage","date","author_name","author_picture","description"]


class Query(graphene.ObjectType):
    all_articles= graphene.List(ArticleType)

    def resolve_all_articles(root, info):
        # We can easily optimize query count in the resolve method
        return Article.objects.all()


schema = graphene.Schema(query=Query)
