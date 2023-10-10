from django.db import models

class Task(models.Model):
    created = models.DateField()
    title = models.CharField(max_length=100)
    detail = models.TextField(blank=True)
