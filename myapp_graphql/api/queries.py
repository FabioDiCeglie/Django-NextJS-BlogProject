from .models import Article

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
