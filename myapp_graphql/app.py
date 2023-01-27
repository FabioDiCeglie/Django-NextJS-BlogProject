from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listArticles_resolver, getArticle_resolver

query = ObjectType("Query")
query.set_field("listArticles", listArticles_resolver)
query.set_field("getArticle", getArticle_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

# from api.models import Article
# from datetime import datetime
# current_date = datetime.today().date()
# with app.app_context():
#         new_post = Article(title="A new morning",coverImage="",date=current_date,author_name="fabio", author_picture="", description="A new morning details")
#         db.session.add(new_post)
#         db.session.commit()
#         users = Article.query.all()
#         print(users)
