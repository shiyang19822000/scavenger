# -*- coding: utf-8 -*-
from django.urls import path

from compensation.views import CompensationModelList

app_name = 'compensation'

urlpatterns = [
    # path('', views.index, name='index'),
    path(r'compensation_list/', CompensationModelList.as_view()),
]
