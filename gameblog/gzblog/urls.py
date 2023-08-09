from django.urls import path
from .views import Home, CreateArticle, RemoveArticle


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('new/article/', CreateArticle.as_view(), name='new_article'),
    path('article/delete/<int:pk>', RemoveArticle.as_view(), name='remove_article'),
]