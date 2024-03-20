from django.urls import path
from .views import overview,members

urlpatterns = [
    path('overview', overview, name='affiliate_overview'),
    path('members', members, name='affiliate_members'),
]