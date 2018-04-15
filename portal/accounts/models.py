from django.contrib import auth
from django.db import models
from django.utils import timezone
import datetime

class About(models.Model):
    username = models.CharField(max_length = 60 ,primary_key=True)
    Password = models.CharField(max_length=60)
    mode = models.NullBooleanField('mode:' , null=True , blank=True)

    def __str__(self):
        return self.username

Field_name_list = (
    ('Cricket','Cricket'),
    ('Football','Football'),
    ('Tennis','Tennis'),
    ('VolleyBall','VolleyBall'),
    ('BasketBall','BasketBall'),
    ('Squash','Squash')
)

class Student(models.Model):
    # username = models.ForeignKey(About , on_delete=models.CASCADE  , related_name="about" )
    username = models.CharField(max_length=60)
    Field_name = models.CharField(max_length=200,choices=Field_name_list, default=None,null=True , blank=True)
    purpose = models.TextField()
    Booking_date = models.DateField()
    Booking_time = models.TimeField()
    pending = models.BooleanField(default=False)
    approved_comment =  models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def RequestViewed(self):
        self.pending = True
        self.save()

    def approve(self):
        self.approved_comment = True
        self.save()

    def disapprove(self):
        self.approved_comment = False
        self.save()
