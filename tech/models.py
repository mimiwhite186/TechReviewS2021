from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='Meeting'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ForeignKey(User, on_delete=models.CASCADE)
    minutestext=models.TextField()


    def __str__(self):
        return self.meetingid

    class Meta:
        db_table='MeetingMinutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField()
    dateentered=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()


    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='Resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    description=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='Event'