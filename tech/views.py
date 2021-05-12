from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your views here.
def index(request):
    return render(request, 'tech/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'tech/resources.html', {'resource_list': resource_list})