
# Create your views here.
from django.shortcuts import render
from django.views import View

from .models import Post


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'myblog/index.html', context={
            'posts': posts
        })