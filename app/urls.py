from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novidades/', views.updates, name='updates'),
    path('sobre/', views.about, name='about'),
    path('api/', views.api, name='api'),
    path('Emote<int:emote_id>', views.graphics, name='graphics'),
    path('Wmote<int:wmote_id>', views.graphics, name='graphics')
]
