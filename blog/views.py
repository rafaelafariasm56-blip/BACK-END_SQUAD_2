from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import BlogPost, Category, Author
from .serializers import (
    BlogPostListSerializer, 
    BlogPostDetailSerializer, 
    BlogPostCreateUpdateSerializer,
    CategorySerializer,
    AuthorSerializer
)
def blog_page(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog/blog_list.html', {'posts': posts})
class BlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostListSerializer
    
    def get_queryset(self):
        queryset = BlogPost.objects.filter(published=True)
        category = self.request.query_params.get('category', None)
        featured = self.request.query_params.get('featured', None)
        search = self.request.query_params.get('search', None)
        
        if category and category.lower() != 'todos':
            queryset = queryset.filter(category__name__iexact=category)
        
        if featured and featured.lower() == 'true':
            queryset = queryset.filter(featured=True)
            
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(content__icontains=search) |
                Q(author__name__icontains=search)
            )
        
        return queryset

class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(published=True)
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'id'

class FeaturedPostsView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(published=True, featured=True)
    serializer_class = BlogPostListSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@api_view(['GET'])
def related_posts(request, post_id):
    """Get related posts based on category"""
    try:
        post = BlogPost.objects.get(id=post_id, published=True)
        related = BlogPost.objects.filter(
            category=post.category, 
            published=True
        ).exclude(id=post_id)[:3]
        
        serializer = BlogPostListSerializer(related, many=True)
        return Response(serializer.data)
    except BlogPost.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def blog_stats(request):
    """Get blog statistics"""
    stats = {
        'total_posts': BlogPost.objects.filter(published=True).count(),
        'featured_posts': BlogPost.objects.filter(published=True, featured=True).count(),
        'categories': Category.objects.count(),
        'authors': Author.objects.count(),
    }
    return Response(stats)

class BlogPostCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateUpdateSerializer

class BlogPostUpdateView(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateUpdateSerializer
    lookup_field = 'id'

class BlogPostDeleteView(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    lookup_field = 'id'

