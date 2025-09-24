from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import BlogPost, Category, Author

def blog_page(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog/blog_list.html', {'posts': posts})

    queryset = BlogPost.objects.all()
    lookup_field = 'id'


