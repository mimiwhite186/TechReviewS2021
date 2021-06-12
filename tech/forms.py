from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingForm(forms.ModelForm):
    class Mata:
        model=Meeting
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Mata:
        model=Resource
        fields='__all__'