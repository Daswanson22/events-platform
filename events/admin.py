from django.contrib import admin
from .models import Profile, City, Company, Tag, Event
# Register your models here.

admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Tag)
admin.site.register(Event)
