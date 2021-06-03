from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request, 'tech/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'tech/resources.html', {'resource_list': resource_list})

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'tech/meeting.html', {'meeting_list' : meeting_list})

def meetingdetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'tech/meetingdetail.html', {'meeting' : meeting})