from django.urls import path
from .views import news_list,news_detail

urlpatterns = [
    path('list', news_list, name='news_list'),
    path('detail', news_detail, name='news_detail'),
]