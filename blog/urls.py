from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_page, name='blog'),  
    path('posts/', views.BlogPostListView.as_view(), name='blog-list'),
    path('posts/<int:id>/', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('featured/', views.FeaturedPostsView.as_view(), name='blog-featured'),
    path('posts/', views.BlogPostListView.as_view(), name='blog-post-list'),
    path('posts/<int:id>/', views.BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('posts/featured/', views.FeaturedPostsView.as_view(), name='featured-posts'),
    path('posts/<int:post_id>/related/', views.related_posts, name='related-posts'),
    
    path('posts/create/', views.BlogPostCreateView.as_view(), name='blog-post-create'),
    path('posts/<int:id>/update/', views.BlogPostUpdateView.as_view(), name='blog-post-update'),
    path('posts/<int:id>/delete/', views.BlogPostDeleteView.as_view(), name='blog-post-delete'),
    
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    
    path('stats/', views.blog_stats, name='blog-stats'),
]
