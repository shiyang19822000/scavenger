# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics

from .models import CompensationModel
from .serializers import CompensationModelSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Compensation!")


class CompensationModelViewSet(viewsets.ModelViewSet):
    queryset = CompensationModel.objects.all().order_by('-update_at')
    serializer_class = CompensationModelSerializer


class CompensationModelList(generics.ListAPIView):
    queryset = CompensationModel.objects.all().order_by('-update_at')
    serializer_class = CompensationModelSerializer

    def get_queryset(self):
        compensations = CompensationModel.objects.all().order_by('-update_at')
        return compensations

    def filter_queryset(self, queryset):
        queryset = CompensationModel.objects.all().order_by('-update_at')
        return queryset
