from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('events/new/', views.events_new, name="new"),
  path('accounts/signup/', views.signup, name="signup"),
  path('profile/', views.profile, name="profile"),
]