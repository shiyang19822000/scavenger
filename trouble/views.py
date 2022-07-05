# -*- coding: utf-8 -*-
from django.http import HttpResponse

# Create your views here.
from rest_framework import viewsets, generics

from worry.models import ArticleModel
from worry.serializers import ArticleModelSerializer


def index(request):
    return HttpResponse("Hello, world. Trouble!")


class TroubleModelList(viewsets.ModelViewSet):
    queryset = ArticleModel.objects.all().order_by('-update_at')
    serializer_class = ArticleModelSerializer


class TroubleModelList(generics.ListAPIView):
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
