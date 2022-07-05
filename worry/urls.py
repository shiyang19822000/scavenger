# -*- coding: utf-8 -*-
from django.urls import path

from worry.views import WorryModelList

app_name = 'worry'

urlpatterns = [
    # path('', views.index, name='index'),
    path(r'worry_list/', WorryModelList.as_view()),
]
