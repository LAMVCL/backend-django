from django.db import models

# Create your models here.
class RestApi(models.Model):
    name = models.CharField(max_length=25)