from django.shortcuts import render, get_object_or_404
from .models import Profile, Project, BlogPost, Experience, Education


def home(request):
    """主页视图"""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    recent_posts = BlogPost.objects.filter(is_published=True)[:3]
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'recent_posts': recent_posts,
    }
    return render(request, 'home/index.html', context)


def projects(request):
    """项目列表视图"""
    profile = Profile.objects.first()
    all_projects = Project.objects.all()
    
    context = {
        'profile': profile,
        'projects': all_projects,
    }
    return render(request, 'home/projects.html', context)


def project_detail(request, project_id):
    """项目详情视图"""
    profile = Profile.objects.first()
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'profile': profile,
        'project': project,
    }
    return render(request, 'home/project_detail.html', context)


def blog(request):
    """博客列表视图"""
    profile = Profile.objects.first()
    posts = BlogPost.objects.filter(is_published=True)
    
    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'home/blog.html', context)


def blog_detail(request, slug):
    """博客详情视图"""
    profile = Profile.objects.first()
    post = get_object_or_404(BlogPost, slug=slug)
    
    context = {
        'profile': profile,
        'post': post,
    }
    return render(request, 'home/blog_detail.html', context)


def resume(request):
    """简历页面视图"""
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'featured_projects': featured_projects,
    }
    return render(request, 'home/resume.html', context)
