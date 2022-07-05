# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics

from .models import ArticleModel
from .serializers import ArticleModelSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Worry!")


class WorryModelViewSet(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.all().order_by('-update_at')
    serializer_class = ArticleModelSerializer


class WorryModelList(generics.ListAPIView):
    queryset = ArticleModel.objects.all().order_by('-update_at')
    serializer_class = ArticleModelSerializer

    def get_queryset(self):
        articles = ArticleModel.objects.all().order_by('-update_at')
        return articles

    def filter_queryset(self, queryset):
        queryset = ArticleModel.objects.all().order_by('-update_at')

        art_id = self.request.query_params.get('art_id', 0)
        if art_id:
            queryset = queryset.filter(art_id=int(art_id))

        art_category = self.request.query_params.get('art_category', 0)
        if art_category:
            queryset = queryset.filter(art_category=int(art_category))

        art_status = self.request.query_params.get('art_status', 2)
        if art_status:
            queryset = queryset.filter(art_status=int(art_status))

        activated = self.request.query_params.get('activated', 1)
        if activated:
            queryset = queryset.filter(activated=int(activated))

        return queryset
