from .models import Article
from ariadne import convert_kwargs_to_snake_case

def listArticles_resolver(obj, info):
    try:
        articles = [article.to_dict() for article in Article.query.all()]
        print(articles)
        payload = {
            "success": True,
            "articles": articles
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getArticle_resolver(obj, info, id):
    try:
        article = Article.query.get(id)
        payload = {
            "success": True,
            "article": article.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload
