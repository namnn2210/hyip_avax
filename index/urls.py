from django.urls import path
from .views import index, account, recharge, withdraw

urlpatterns = [
    path('', index, name='index'),
    path('account', account, name='account'),
    path('recharge', recharge, name='recharge'),
    path('withdraw', withdraw, name='withdraw'),
]