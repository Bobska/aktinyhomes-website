from django.contrib import admin
from .models import TinyHomeLayout, TinyHomeImage, BlogPost, FAQ

@admin.register(TinyHomeLayout)
class TinyHomeLayoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'price_range', 'created_at']
    list_filter = ['size', 'created_at']
    search_fields = ['name', 'description']

@admin.register(TinyHomeImage)
class TinyHomeImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'layout', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'layout', 'created_at']
    search_fields = ['title', 'description']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'content']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['question', 'answer']
    ordering = ['order', 'created_at']
