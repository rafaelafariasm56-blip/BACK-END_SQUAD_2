from django.contrib import admin
from .models import Category, Author, BlogPost

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'featured', 'published', 'created_at']
    list_filter = ['category', 'featured', 'published', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['featured', 'published']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Conteúdo', {
            'fields': ('content', 'excerpt', 'image')
        }),
        ('Configurações', {
            'fields': ('featured', 'published')
        }),
    )
