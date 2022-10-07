from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('rum/', views.rum, name = 'rum'),
    path('bars/', views.bars, name = 'bars'),
    path('posts/', views.blog_posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('cocktails/', views.cocktails, name='cocktails'),
    path('creators/', views.creators, name='creators')
]