from django.contrib import admin

# Register your models here.
from .models import ArticleModel


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('art_id', 'art_title', 'art_publisher', 'art_source', 'art_category', 'art_status', 'update_at')
    search_fields = ['art_title', ]
    fields = (
        'art_title', 'art_publisher', 'publish_time', 'art_source', 'art_content', 'art_declaration', 'art_thumbnail',
        'art_illustrated', 'art_category', 'art_status', 'activated')
    date_hierarchy = 'publish_time'


admin.site.register(ArticleModel, ArticleModelAdmin)
