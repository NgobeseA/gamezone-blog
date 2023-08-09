from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Article
from .form import NewArticle
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = Article
    template_name = 'home.html'

class CreateArticle(CreateView):
    model = Article
    template_name = 'new_article.html'
    form_class = NewArticle
    
class RemoveArticle(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')
