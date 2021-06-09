from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(meetingtitle='Python Study')
    
    def test_titlestring(self):
        self.assertEqual(str(self.title), 'Python Study')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

    
class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(resourcename='Python')
        self.user=User(attendance="user1")
        self.resource=Resource(resourcename='Study', resourcetype=self.type, resourceurl='https://www.linkedin.com/learning/collections/6510912637868474368', dateentered=datetime.date('2021,12,31'), user=self.user, description='This is Python study resource page')

    def test_string(self):
        self.assertEqual(str(self.resource), 'Study')

class EventTest(TestCase):
    def setUp(self):
        self.title=Event(eventtitle='Seminar')
        self.user=User(attendance="user1")
        self.event=Event(eventtitle='seminar', lcation='SCC', eventdate='2021,6,30', eventtime='noon', description='This is about Python study')

    def test_string(self):
        self.assertEqual(str(self.event), 'Seminar')