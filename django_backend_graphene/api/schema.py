import graphene
from graphene_django import DjangoObjectType

from .models import Article

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ["id", "title","coverImage","date","author_name","author_picture","description"]


class Query(graphene.ObjectType):
    all_articles= graphene.List(ArticleType)
    article = graphene.Field(ArticleType, id=graphene.String(required=True))

    def resolve_all_articles(root, info):
        return Article.objects.all()

    def resolve_article(root, info, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
