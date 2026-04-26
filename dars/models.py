from django.db import models

# Create your models here.

class Notebook(models.Model):
    name = models.CharField(max_length=244)
    brend = models.CharField(max_length=244)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name



