from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventForm, SignupForm
from django.contrib.auth import login

from .models import Event, User

# Create your views here.
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def profile(request):
  events = Event.objects.filter(user__id=request.user.id)
  context = {
    'events': events,
  }
  return render(request, 'registration/profile.html', context)

def events_new(request):
  event_form = EventForm(request.POST or None)
  if request.POST and event_form.is_valid():
    new_event = event_form.save(commit=False)
    new_event.user = request.user
    new_event.save()

    return redirect('home')
  else:
    return render(request, 'events/new.html', { 'event_form': event_form })


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