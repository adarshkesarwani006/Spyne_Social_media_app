from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    hashtags = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    replies = models.ManyToManyField('self', symmetrical=False, related_name='replied_to')
