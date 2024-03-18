from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)
    parent_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

