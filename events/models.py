from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.state}"

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='companies')
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='events')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    hosted_by = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='events')
    attendees = models.ManyToManyField(User, related_name='attending_events', blank=True)
    tags = models.ManyToManyField(Tag, related_name='events', blank=True)
    reoccuring = models.BooleanField(default=False)

    def __str__(self):
        return self.title