from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, default="", blank=True, unique = True)
    description = models.CharField(max_length=200,  default="", blank=True)
    

    def __str__(self):
        return self.title
    