from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date

# Create your models here.
class Profile(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  username = models.CharField(max_length=50)

  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username

# creates a profile for user when the user signs up
def create_profile(sender, **kwargs):
  # if user is created then create user's profile
  if kwargs['created']:
    # passes user.object into create method for profile; associating user that is created with profile
    profile = Profile.objects.create(user=kwargs['instance'])

# saves user.object, when it's saved it then run code based of the post_save signal
# Parameters: sender: Specifies a specific sender to receive signals from
post_save.connect(create_profile, sender=User)

class Event(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField("Event Date")
  time = models.TimeField("Event Time", default="12:00:00")
  description = models.TextField(max_length=2000)

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name}"