from django.db import models
from django.contrib.auth.models import User

from category.models import Category


class Operation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='transaction_set')
    operation_type = models.ForeignKey(Operation, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    @property
    def category_name(self):
        return self.category.title
