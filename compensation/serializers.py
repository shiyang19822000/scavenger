# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import CompensationModel


class CompensationModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompensationModel
        fields = ['cpns_id', 'cpns_title', 'cpns_category', 'cpns_content', 'activated', 'create_at', 'update_at']
