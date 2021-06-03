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
    
    