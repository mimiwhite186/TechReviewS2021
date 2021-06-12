from TechReviewS2021.tech.forms import MeetingForm
from TechReviewS2021.tech.forms import ResourceForm
from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm
from .forms import ResourceForm

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

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'tech/newmeeting.html', {'form': form})

def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'tech/newresource.html', {'form': form})