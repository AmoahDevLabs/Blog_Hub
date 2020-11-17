from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(default='Enter your biography', verbose_name='biography')
    website_url = models.URLField(max_length=255, null=True, blank=True, default='Website')
    facebook_url = models.URLField(max_length=255, null=True, blank=True, default='Facebook')
    twitter_url = models.URLField(max_length=255, null=True, blank=True, default='Twitter')
    instagram_url = models.URLField(max_length=255, null=True, blank=True, default='Instagram')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
