from django.db import models

# Create your models here.
class UserProfile(models.Model):
    age = models.IntegerField()
    height = models.IntegerField()
    sex = models.BooleanField()

class DailyRegister(models.Model):
    weight = models.FloatField()
    calories_consumed = models.FloatField()