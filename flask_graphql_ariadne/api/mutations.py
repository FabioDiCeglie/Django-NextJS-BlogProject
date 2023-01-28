from datetime import date

from ariadne import convert_kwargs_to_snake_case

from api import db
from .models import Article

@convert_kwargs_to_snake_case
def create_article_resolver(obj, info, title, cover_image, author_name, author_picture, description):

    try:
        today = date.today()
        article = Article(
            title=title, coverImage=cover_image, date=today.strftime("%b-%d-%Y"),
            author_name=author_name, author_picture=author_picture, description=description,

        )
        db.session.add(article)
        db.session.commit()
        payload = {
            "success": True,
            "article": article.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

@convert_kwargs_to_snake_case
def update_article_resolver(obj, info, id, title, description):
    try:
        article = Article.query.get(id)
        if article:
            article.title = title
            article.description = description
        db.session.add(article)
        db.session.commit()
        payload = {
            "success": True,
            "article": article.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def delete_article_resolver(obj, info, id):
    try:
        post = Article.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {"success": True, "post": post.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload
