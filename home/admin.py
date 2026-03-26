from django.contrib import admin
from .models import Profile, Project, BlogPost


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location', 'updated_at']
    search_fields = ['name', 'title', 'email']
    list_filter = ['created_at', 'updated_at']
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'title', 'avatar')
        }),
        ('联系方式', {
            'fields': ('email', 'phone', 'location')
        }),
        ('个人简介', {
            'fields': ('bio',)
        }),
        ('社交媒体', {
            'fields': ('github_url', 'linkedin_url')
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'created_at', 'updated_at']
    list_filter = ['is_featured', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['is_featured']
    prepopulated_fields = {}
    fieldsets = (
        ('项目信息', {
            'fields': ('title', 'description', 'image', 'is_featured')
        }),
        ('技术信息', {
            'fields': ('technologies',)
        }),
        ('链接', {
            'fields': ('github_url', 'live_url')
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'created_at', 'updated_at']
    list_filter = ['is_published', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'excerpt']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('文章信息', {
            'fields': ('title', 'slug', 'cover_image', 'is_published')
        }),
        ('文章内容', {
            'fields': ('excerpt', 'content')
        }),
    )
