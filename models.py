from django.db import models

class Animal(models.Model):
    species = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)