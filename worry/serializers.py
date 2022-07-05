# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import ArticleModel


class ArticleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['art_id', 'art_title', 'art_publisher', 'publish_time', 'art_source', 'art_content',
                  'art_declaration', 'art_thumbnail', 'art_illustrated', 'art_category', 'art_status', 'activated',
                  'create_at', 'update_at']
        # fields = ['art_title', 'art_publisher', 'publish_time', 'art_source', 'art_content', 'art_declaration', 'art_thumbnail', 'art_illustrated', 'art_category', 'art_status', 'activated', 'create_at', 'update_at']
        # fields = '__all__'
