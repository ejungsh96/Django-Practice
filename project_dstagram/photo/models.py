from django.db import models
from django.urls import reverse

# Create your models here.

# Default(Basic) model of django
from django.contrib.auth.models import User

from config.settings import AUTH_PASSWORD_VALIDATORS

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)   # Set up the time of when the file uploaded
    updated = models.DateTimeField(auto_now=True)       # Set up the time whenever the file updated
    
    class Meta:
        ordering = ['-updated']
    
    # To print instance or to show the information of the instance
    def __str__(self):
        return self.author.username +  " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
    
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])
    