from django.db import models

class Hotel(models.Model):
    hotel_name = models.CharField('название', max_length=50)
    hetel_about = models.TextField('описание')
