from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to = 'media/')
    bio = models.TextField(default="Hey there!I\'m using Instagram")
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile


class Image(models.Model):
    """
    Image model class
    """
    image = models.ImageField(upload_to='media/')
    image_name = models.CharField(max_length=60)
    image_caption = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def save_image(self):
        return self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()

        return images
    
    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images
