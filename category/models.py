from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.title
