from django.contrib import admin
from api.models import Article

# Register your models here.
# admin.site.register(Article)
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ("title", "description")
    list_display = ("title", "description")
