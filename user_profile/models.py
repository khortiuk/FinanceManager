from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')

    def delete(self, using=None, keep_parents=False):
        User.objects.get(username=self.user.username).delete()
        super(UserProfile, self).delete()

    @property
    def password(self):
        return self.user.password

    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return self.user.username
