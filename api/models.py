from django.db import models

# Create your models here.


class TextToSpeech(models.Model):
    length_minutes = models.IntegerField
