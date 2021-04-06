from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm, SignupForm
from django.contrib.auth import login

# Create your views here.
def home(request):
  return HttpResponse('<h1>Home</h1>')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)