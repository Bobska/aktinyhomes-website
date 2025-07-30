from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('layouts/', views.layouts, name='layouts'),
    path('blog/', views.blog, name='blog'),
    path('faqs/', views.faqs, name='faqs'),
    path('red-tape/', views.red_tape, name='red_tape'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
]
