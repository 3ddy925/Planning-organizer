from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from .forms import EventForm, SignupForm, EditProfileForm
from django.contrib.auth import login

from .models import Event, User

# Create your views here.
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

@login_required
def profile(request):
  events = Event.objects.filter(user_id=request.user.id).order_by('date')
  today = date.today()
  events_list = []
  for event in events:
    if event.date >= today:
      events_list.append(event)
  context = {
    'events': events,
    'events': events_list,
  }
  return render(request, 'registration/profile.html', context)

@login_required
def edit_profile(request):
  user = User.objects.get(id=request.user.id)
  profile_form = EditProfileForm(request.POST or None, instance=user)
  if request.POST and profile_form.is_valid():
    profile_form.save()
    return redirect('profile')
  else:
    return render(request, 'registration/edit_profile.html', { 'user': user, 'profile_form': profile_form })

@login_required
def new(request):
  event_form = EventForm(request.POST or None)
  if request.POST and event_form.is_valid():
    new_event = event_form.save(commit=False)
    new_event.user = request.user
    new_event.save()

    return redirect('profile')
  else:
    return render(request, 'events/new.html', { 'event_form': event_form })

@login_required
def events_edit(request, event_id):
    user = User.objects.get(id=request.user.id)
    events = Event.objects.get(id=event_id)
    form = EventForm(request.POST or None, instance=events)
    context = {
      'events': events,
      'form': form,
      'user': user,
    }
    if request.method == 'POST' and form.is_valid():
      form.save()
      return redirect('profile')
    else:
      return render(request, 'events/edit.html', context)

def events_delete(request, event_id):
    events = Event.objects.get(id=event_id)

    if request.method == "POST":
      events.delete()
      return redirect('profile')
    else:
      return render(request, 'events/event.html', { 'events': events })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)