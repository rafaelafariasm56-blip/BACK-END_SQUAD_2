from rest_framework import serializers
from .models import BlogPost, Category, Author

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio']

class BlogPostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'author', 'category', 'excerpt', 
            'image', 'featured', 'created_at'
        ]

class BlogPostDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'author', 'category', 'content', 
            'excerpt', 'image', 'featured', 'created_at', 'updated_at'
        ]

class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title', 'slug', 'author', 'category', 'content', 
            'excerpt', 'image', 'featured', 'published'
        ]
