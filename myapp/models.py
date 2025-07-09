# models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

CHOICES = [
    ('1', 'definitely'),
    ('2', 'maybe'),
    ('3', 'not sure'),
]

rolech = [
    ('1', 'individual'),
    ('2', 'couple'),
    ('3', 'small group'),
    ('4', 'large group'),
    ('5', 'prefer not to say'),
]

pur = [
    ('1', 'Date'),
    ('2', 'Birthday'),
    ('3', 'Anniversary'),
    ('4', 'Party'),
]

class Booking(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254)
    subject = models.TextField(default='')
    message = models.TextField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
        
    

    def clean(self):
        if not self.name.strip():
            raise ValidationError('Name cannot be empty or just whitespace.')
        if not self.email:
            raise ValidationError('Email cannot be empty.')
        super().clean()

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=12, default='')
    phone = models.CharField(max_length=10, null=True, blank=True)
    people = models.IntegerField(default=0)
    message = models.TextField(max_length=300, null=True, blank=True)
    table_number = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    

    class Meta:
        unique_together = ('name', 'email', 'date')

    def clean(self):
        if not self.name.strip():
            raise ValidationError('Name cannot be empty or just whitespace.')
        if not self.email:
            raise ValidationError('Email cannot be empty.')
        super().clean()

    def __str__(self):
        return self.name
