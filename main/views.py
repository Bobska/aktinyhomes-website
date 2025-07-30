from django.shortcuts import render
from .models import TinyHomeLayout, TinyHomeImage, BlogPost, FAQ

def home(request):
    """Home page view"""
    featured_images = TinyHomeImage.objects.filter(is_featured=True)[:12]
    layouts = TinyHomeLayout.objects.all()[:3]
    
    context = {
        'featured_images': featured_images,
        'layouts': layouts,
    }
    return render(request, 'main/home.html', context)

def layouts(request):
    """Layouts page view"""
    all_layouts = TinyHomeLayout.objects.all()
    context = {
        'layouts': all_layouts,
    }
    return render(request, 'main/layouts.html', context)

def blog(request):
    """Blog page view"""
    posts = BlogPost.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'main/blog.html', context)

def faqs(request):
    """FAQs page view"""
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'main/faqs.html', context)

def red_tape(request):
    """Red tape page view"""
    return render(request, 'main/red_tape.html')

def privacy_policy(request):
    """Privacy policy page view"""
    return render(request, 'main/privacy_policy.html')

def terms_conditions(request):
    """Terms and conditions page view"""
    return render(request, 'main/terms_conditions.html')
