from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView 
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novidades/', views.updates, name='updates'),
    path('sobre/', views.about, name='about'),
    path('api/', views.api, name='api'),
    
   url(r'^Emote01/',TemplateView.as_view(template_name="Emote01.html"), name='emote'),
]
