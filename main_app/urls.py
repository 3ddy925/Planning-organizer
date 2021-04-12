from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('events/new/', views.new, name="new"),
  path('events/edit/<int:event_id>/', views.events_edit, name="events_edit"),
  path('events/delete/<int:event_id>/', views.events_delete, name="events_delete"),
  path('accounts/signup/', views.signup, name="signup"),
  path('profile/', views.profile, name="profile"),
  path('profile/edit', views.edit_profile, name="edit_profile"),
  path('change-password', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html', success_url='/'), name='change-password'),
]