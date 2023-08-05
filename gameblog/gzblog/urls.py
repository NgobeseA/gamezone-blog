from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('new/article/', views.CreateArticle.as_view(), name='new_article')
]