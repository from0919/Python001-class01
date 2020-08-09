from django.urls import path
from . import views
urlpatterns = [
    path('index', views.moives_short),
    path('search/', views.search_comment, name='search_url'),
]