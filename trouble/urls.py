# -*- coding: utf-8 -*-
from django.urls import path

from trouble.views import TroubleModelList

app_name = 'trouble'

urlpatterns = [
    # path('', views.index, name='index'),
    path(r'trouble_list/', TroubleModelList.as_view()),
]
