from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Article
from .form import NewArticle

# Create your views here.
class Home(ListView):
    model = Article
    template_name = 'home.html'

class CreateArticle(CreateView):
    model = Article
    template_name = 'new_article.html'
    form_class = NewArticle
    