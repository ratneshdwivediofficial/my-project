from django.db import models
from django.core.validators import MaxValueValidator
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    followers = models.ManyToManyField('UserProfile',
                                        related_name="followers_profile",
                                        blank=True)
    following = models.ManyToManyField('UserProfile',
                                        related_name="following_profile",
                                        blank=True)
    profile_pic = ProcessedImageField(upload_to='profile_pics',
                                format='JPEG',
                                options={ 'quality': 100},
                                null=True,
                                blank=True)

    bio = models.CharField(max_length=200, null=True, blank=True)

    AC_TYPE = (
        ('Ind','Individual'),
        ('Org','Organization'),
    )
    email = models.EmailField(max_length=70, unique=True)     
    ac_type = models.CharField(max_length=3, choices=AC_TYPE)

    job_profile = models.CharField(max_length=50, blank=True, null=True)
    
    def get_number_of_followers(self):
        print(self.followers.count())
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.user.username

        

class Contact(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField(primary_key=True, validators=[
                                        MaxValueValidator(9999999999)])
   