from django.db import models
import os
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
# Create your models here.
#def get_image_path(filename):
#    return os.path.join('photos',filename)

#def photos_file_name(instance, filename):
#    return '/'.join(['photos', instance.id, filename])
def photos_file_name(instance, filename):
    return os.path.join('photos', str(instance.id), filename)
class Photos(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(blank = False)
#    text = models.TextField(blank = False)
    image = models.ImageField(upload_to=photos_file_name, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='photos', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
    def __str__(self):
        return (self.name)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
