from django.urls import path
from .views import Home, CreateArticle, RemoveArticle, ArticleInfo


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('new/article/', CreateArticle.as_view(), name='new_article'),
    path('article/delete/<int:pk>', RemoveArticle.as_view(), name='remove_article'),
    path('article/detail/<int:pk>', ArticleInfo.as_view(), name='article_info'),
]