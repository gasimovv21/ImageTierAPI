from django.db import models

class UserImage(models.Model):
    image = models.ImageField(upload_to='images/')
