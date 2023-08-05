from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    body = models.TextField()
    day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "   |   " + self.author
    
    def get_absolute_url(self):
        return reverse('home')