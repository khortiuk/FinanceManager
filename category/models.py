from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title
