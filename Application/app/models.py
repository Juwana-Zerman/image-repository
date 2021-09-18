"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length=75)
    main_imgs = models.ImageField(upload_to='images/')