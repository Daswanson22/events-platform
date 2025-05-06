from django.shortcuts import render
from .models import Event, City, Company, Tag, Profile

# Create your views here.
def index(request):
    return render(request, 'events/index.html')

def events_list(request):
    events = Event.objects.all().order_by('-date')
    print(events)
    return render(request, 'events/events_list.html', {
        'events': events,
    })