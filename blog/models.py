from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField("Header", max_length=255)
    text = models.TextField("Text")
    date = models.DateTimeField("Created at", default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title